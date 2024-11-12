from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import academic_yearsem, filtered_feedbacks, college_numerical_summary_questions, college_numerical_total, RecurringPhrase, college_numerical_summary, college_feedback_total, college_feedback_summary, department, professor_feedback_summary, professor_numerical_total, professor_numerical_summary_questions, professor_numerical_summary_category, professor_feedback_total


class CollegeRatingsSummaryView(APIView):
    def get(self, request, *args, **kwargs):
        year_sem_data = academic_yearsem.objects.all()
        if not year_sem_data.exists():
            return Response({"error": "Year-Semester not found"}, status=404)

        summary = []

        for year_sem in year_sem_data:
            colleges = department.objects.all()
            year_sem_summary = {
                "year_sem": year_sem.year_sem_id,
                "colleges": []
            }

            for college in colleges:
                college_summary = {
                    "name": college.department_id,
                    "description": college.department_desc,
                    "numerical_summary": [],
                    "feedback_summary": [],
                    "professor_list": []
                }

                # Fetching the numerical summary
                college_numerical_totals = college_numerical_total.objects.filter(year_sem_id=year_sem, department=college)
                total_avg = 0
                category_averages = []

                for total in college_numerical_totals:
                    total_avg = total.total_average

                    # Fetching category and question-level averages
                    category_summaries = college_numerical_summary.objects.filter(year_sem_id=year_sem, department=college)
                    for category in category_summaries:
                        question_averages = []

                        # Fetching question-level averages for the category
                        question_summaries = college_numerical_summary_questions.objects.filter(
                            year_sem_id=year_sem,
                            department=college,
                            category=category.category
                        )

                        for question_summary in question_summaries:
                            question_avg_data = {
                                "question_id": question_summary.numerical_question_id.numerical_question_id,
                                "question_desc": question_summary.numerical_question_id.question,
                                "average": question_summary.college_question_average,
                            }
                            question_averages.append(question_avg_data)

                        # Add category data with question averages
                        category_avg_data = {
                            "category_id": category.category.category_id,
                            "category_desc": category.category.category_desc,
                            "average": category.college_average,
                            "question_avg": question_averages,
                        }
                        category_averages.append(category_avg_data)

                college_summary["numerical_summary"].append({
                    "total_avg": total_avg,
                    "category_avg": category_averages
                })

                # Fetching feedback summary including question-level feedback
                feedback_totals = college_feedback_total.objects.filter(year_sem_id=year_sem, department=college).first()
                feedback_summary_data = {
                    "total_feedbacks": feedback_totals.total_feedbacks if feedback_totals else 0,
                    "total_positive": feedback_totals.total_positive if feedback_totals else 0,
                    "total_neutral": feedback_totals.total_neutral if feedback_totals else 0,
                    "total_negative": feedback_totals.total_negative if feedback_totals else 0,
                    "question_summary": []
                }

                # Adding question-level summaries
                question_summaries = college_feedback_summary.objects.filter(year_sem_id=year_sem, department=college)
                for question_summary in question_summaries:
                    question_data = {
                        "question_id": question_summary.feedback_question_id.feedback_question_id,
                        "total_feedbacks": question_summary.total_feedbacks,
                        "total_positive": question_summary.total_positive,
                        "total_neutral": question_summary.total_neutral,
                        "total_negative": question_summary.total_negative,
                    }
                    feedback_summary_data["question_summary"].append(question_data)

                college_summary["feedback_summary"].append(feedback_summary_data)

                # Fetching professors related to the college
                professor_totals = professor_numerical_total.objects.filter(year_sem_id=year_sem, prof_id__department=college)
                professor_feedback_totals = professor_feedback_total.objects.filter(year_sem_id=year_sem, prof_id__department=college)

                for prof_total in professor_totals:
                    full_name = f"{prof_total.prof_id.surname} {prof_total.prof_id.first_name} {prof_total.prof_id.middle_name or ''}".strip()
                    professor = prof_total.prof_id
                    
                    feedback_totals = professor_feedback_totals.filter(prof_id=professor).first()

                    professor_data = {
                        "id": professor.professor_id,
                        "name": full_name,
                        "total_avg": prof_total.total_average,
                        "total_feedbacks": feedback_totals.total_feedbacks if feedback_totals else 0,
                        "total_positive": feedback_totals.total_positive if feedback_totals else 0,
                        "total_neutral": feedback_totals.total_neutral if feedback_totals else 0,
                        "total_negative": feedback_totals.total_negative if feedback_totals else 0,
                    }

                    college_summary["professor_list"].append(professor_data)

                year_sem_summary["colleges"].append(college_summary)

            summary.append(year_sem_summary)

        return Response(summary)

class ProfessorRatingsSummaryView(APIView):
    def get(self, request, *args, **kwargs):
        year_sem_data = academic_yearsem.objects.all()
        summary = []

        for year_sem in year_sem_data:
            professors = []
            prof_totals = professor_numerical_total.objects.filter(year_sem_id=year_sem)

            for prof_total in prof_totals:
                full_name = f"{prof_total.prof_id.surname} {prof_total.prof_id.first_name} {prof_total.prof_id.middle_name or ''}".strip()
                prof = prof_total.prof_id
                professor_data = {
                    "id": prof.professor_id,
                    "name": full_name,
                    #"avatarUrl": prof.avatar_url,  # assuming avatar_url is a field
                    #"initials": prof.initials,
                    "dept_id": prof.department.department_id,
                    "dept_desc": prof.department.department_desc,
                    "numerical_summary": {
                        "total_avg": prof_total.total_average,
                        "category_avg": []
                    },
                    "feedback_summary": []
                }

                # Numerical Summary by Category
                category_summaries = professor_numerical_summary_category.objects.filter(prof_id=prof, year_sem_id=year_sem)
                for category_summary in category_summaries:
                    category_data = {
                        "category_id": category_summary.category.category_id,
                        "category_desc": category_summary.category.category_desc,
                        "average": category_summary.category_average,
                        "question_avg": []
                    }

                    question_summaries = professor_numerical_summary_questions.objects.filter(
                        prof_id=prof, 
                        year_sem_id=year_sem,
                        numerical_question_id__category=category_summary.category.category_id
                    )
                    for question_summary in question_summaries:
                        question_data = {
                            "question_id": question_summary.numerical_question_id.numerical_question_id,
                            "question_desc": question_summary.numerical_question_id.question,
                            "average": question_summary.question_average
                        }
                        category_data["question_avg"].append(question_data)

                    professor_data["numerical_summary"]["category_avg"].append(category_data)

                # Feedback Summary
                feedback_totals = professor_feedback_total.objects.filter(prof_id=prof, year_sem_id=year_sem)
                for feedback_total in feedback_totals:
                    feedback_data = {
                        "total_feedbacks": feedback_total.total_feedbacks,
                        "total_positive": feedback_total.total_positive,
                        "total_neutral": feedback_total.total_neutral,
                        "total_negative": feedback_total.total_negative,
                        "question_summary": []
                    }

                    feedback_questions = professor_feedback_summary.objects.filter(prof_id=prof, year_sem_id=year_sem)
                    for feedback_question in feedback_questions:
                        question_summary_data = {
                            "feedback_question": feedback_question.feedback_question_id.feedback_question_id,
                            "total_feedbacks": feedback_question.total_feedbacks,
                            "total_positive": feedback_question.total_positive,
                            "total_neutral": feedback_question.total_neutral,
                            "total_negative": feedback_question.total_negative
                        }
                        feedback_data["question_summary"].append(question_summary_data)

                    professor_data["feedback_summary"].append(feedback_data)

                professors.append(professor_data)

            summary.append({
                "year_sem": year_sem.year_sem_id, 
                "professors": professors
            })

        return Response(summary)

    
class ProfessorFeedbacks(APIView):
    def get(self, request):
        year_sem = request.query_params.get("year_sem", None)
        prof_id = request.query_params.get("professor_id", None)
        
        # Filter feedbacks based on academic term and professor
        filtered_feedback_list = filtered_feedbacks.objects.select_related("feedback_id", "feedback_id__feedback_question_id").filter(
            feedback_id__student_subj_id__prof_subj_id__year_sem_id=year_sem,
            feedback_id__student_subj_id__prof_subj_id__professor_id=prof_id
        )
        
        # Prepare the data structure
        data_output = {}
        
        for feedback in filtered_feedback_list:
            year_sem_key = year_sem
            professor_key = feedback.feedback_id.student_subj_id.prof_subj_id.professor_id
            full_name = f"{professor_key.surname} {professor_key.first_name} {professor_key.middle_name or ''}".strip()
            
            # Initialize year-semester structure
            if year_sem_key not in data_output:
                data_output[year_sem_key] = {
                    "year_sem": year_sem_key,
                    "professor_feedback_list": []
                }

            # Find or create professor entry
            professor_feedbacks = next(
                (prof for prof in data_output[year_sem_key]["professor_feedback_list"] if prof["id"] == str(professor_key.professor_id)),
                None
            )
            if not professor_feedbacks:
                professor_feedbacks = {
                    "id": str(professor_key.professor_id),
                    "name": full_name,
                    "dept_id": professor_key.department.department_id,
                    "dept_desc": professor_key.department.department_desc,
                    "feedbacks": []
                }
                data_output[year_sem_key]["professor_feedback_list"].append(professor_feedbacks)

            # Add feedback entry
            professor_feedbacks["feedbacks"].append({
                "question_id": feedback.feedback_id.feedback_question_id.feedback_question_id,
                "sentiment": feedback.sentiment_label,
                "text": feedback.feedback_id.feedback_text
            })

        result = list(data_output.values())
        return Response(result, status=status.HTTP_200_OK)

class professorPhrases(APIView):
    def get(self, request):
        year_sem = request.query_params.get('year_sem', None)
        dept_id = request.query_params.get('dept_id', None)
        prof_id = request.query_params.get('professor_id', None)

        # Filter based on the year_sem, dept_id, and professor_id if parameters are provided
        phrases_queryset = RecurringPhrase.objects.select_related('year_sem_id', 'prof_id', 'department').all()
        
        if year_sem:
            phrases_queryset = phrases_queryset.filter(year_sem_id__year_sem_id=year_sem)
        if dept_id:
            phrases_queryset = phrases_queryset.filter(department__department_id=dept_id)
        if prof_id:
            phrases_queryset = phrases_queryset.filter(prof_id__professor_id=prof_id)

        data_output = {}
        
        for phrase in phrases_queryset:
            # Get keys for year_sem and professor
            year_sem_key = phrase.year_sem_id.year_sem_id
            professor_key = phrase.prof_id.professor_id

            # Construct full name
            full_name = f"{phrase.prof_id.surname} {phrase.prof_id.first_name} {phrase.prof_id.middle_name or ''}".strip()

            # Initialize the year_sem structure if it doesn't exist
            if year_sem_key not in data_output:
                data_output[year_sem_key] = {
                    "year_sem": year_sem_key,
                    "professor_phrases": []
                }

            # Check if professor entry exists in the professor_phrases array
            professor_phrases = next(
                (prof for prof in data_output[year_sem_key]["professor_phrases"] if prof["id"] == str(professor_key)),
                None
            )
            
            if not professor_phrases:
                professor_phrases = {
                    "id": str(professor_key),
                    "name": full_name,  # Use full_name here
                    "dept_id": phrase.department.department_id,
                    "dept_desc": phrase.department.department_desc,
                    "recurring_phrases": []
                }
                data_output[year_sem_key]["professor_phrases"].append(professor_phrases)

            # Add the recurring phrase to the professor's phrases
            professor_phrases["recurring_phrases"].append({
                "count": str(phrase.total_count),
                "sentiment": phrase.sentiment_label,
                "phrase": phrase.phrase
            })

        result = list(data_output.values())
        return Response(result)

class collegePhrases(APIView):
    def get(self, request):
        year_sem = request.query_params.get('year_sem', None)
        dept_id = request.query_params.get('dept_id', None)

        # Filter RecurringPhrase objects by year_sem_id and department if parameters are provided
        phrases_queryset = RecurringPhrase.objects.select_related('year_sem_id', 'department').all()
        
        if year_sem:
            phrases_queryset = phrases_queryset.filter(year_sem_id__year_sem_id=year_sem)
        if dept_id:
            phrases_queryset = phrases_queryset.filter(department__department_id=dept_id)

        # Define the dictionary structure to store all recurring phrases by academic year and department
        recurring_phrases_list = []

        # Create a mapping to organize data by year-sem
        year_sem_mapping = {}
        
        for phrase in phrases_queryset:
            year_sem_key = phrase.year_sem_id
            department_key = phrase.department

            # Ensure year_sem_key exists in the year_sem_mapping
            if year_sem_key not in year_sem_mapping:
                year_sem_mapping[year_sem_key] = {
                    "year_sem": year_sem_key.year_sem_id,
                    "college_phrases": []
                }

            # Ensure the department exists under the specific year-sem in the dictionary
            department_phrases = next(
                (item for item in year_sem_mapping[year_sem_key]["college_phrases"] if item["dept_id"] == department_key.department_id),
                None
            )
            
            if not department_phrases:
                department_phrases = {
                    "dept_id": department_key.department_id,
                    "dept_desc": department_key.department_desc,
                    "recurring_phrases": []
                }
                year_sem_mapping[year_sem_key]["college_phrases"].append(department_phrases)

            # Add the current phrase to the department's recurring_phrases
            department_phrases["recurring_phrases"].append({
                "count": phrase.total_count,
                "sentiment": phrase.sentiment_label,
                "phrase": phrase.phrase
            })

        # Append the structured data to the recurring_phrases_list
        recurring_phrases_list.extend(year_sem_mapping.values())

        # Return the response
        return Response(recurring_phrases_list)
    













