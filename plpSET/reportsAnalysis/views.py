from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CollegeRatingsSummary(APIView):
    def get(self, request):

        college_rating = [
        {
            "year_sem": "24-25-1",
            "summary": [{
        "name": "CAS",
        "description": "College of Arts and Sciences",
        "numerical_summary": [
            {
                "total_avg": 4.7,
                "category_avg": [
                    {
                        "category_id": "A",
                        "category_desc": "The Teacher",
                        
                        "average": 4.5
                    },
                    {
                        "category_id": "B",
                        "category_desc": "The Module/Learning Materials",
                        
                        "average": 4.9
                    },
                    {
                        "category_id": "C",
                        "category_desc": "The Use of LMS",
                        
                        "average": 2
                    },
                    {
                        "category_id": "D",
                        "category_desc": "The Use of Social Media Platforms",
                        
                        "average": 4
                    },
                    {
                        "category_id": "E",
                        "category_desc": "General Observation",
                        
                        "average": 3.5
                    },
                ],
               
            },],
        "feedback_summary":[
            {
                "total_feedbacks": 100,
                "total_positive": 80,
                "total_neutral": 5,
                "total_negative": 15,
            }
        ],
        "professor_list":[
           {
            "id": "1",
            "name": 'Ronnie Chu',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 4.70,
            
            "total_feedbacks": 100,
            "total_positive": 80,
            "total_neutral": 5,
            "total_negative": 15,
            },
           {
            "id": "2",
            "name": 'Noreen Perez',
            "avatarUrl": 'https://cdnb.artstation.com/p/assets/images/images/059/961/409/large/t-o-f-u-tofufaerie-froggo-5105.jpg?1677526327.jpg',
            "initials": 'RC',
            "total_avg": 4.4,
            "total_feedbacks": 100,
            "total_positive": 77,
            "total_neutral": 13,
            "total_negative": 10,
            },
           {
            "id": "3",
            "name": 'Goyo',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 3.5,
            "total_feedbacks": 100,
            "total_positive": 40,
            "total_neutral": 10,
            "total_negative": 50,
            },
           {
            "id": "4",
            "name": 'Andres Bonifacio',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 4,
            "total_feedbacks": 100,
            "total_positive": 70,
            "total_neutral": 30,
            "total_negative": 10,
            },
           {
            "id": "5",
            "name": 'Jose Rizal',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 4.3,
            "total_feedbacks": 100,
            "total_positive": 60,
            "total_neutral": 20,
            "total_negative": 20,
            },
           {
            "id": "6",
            "name": 'Jesus',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 4.9,
            "total_feedbacks": 100,
            "total_positive": 90,
            "total_neutral": 5,
            "total_negative": 5,
            },
        ]
            
    },
        {
        "name": "CCS",
        "description": "College of Computer Studies",
        "year_sem": "24-25-1",
        "numerical_summary": [
            {
                "total_avg": 3,
                "category_avg": [
                    {
                        "category_id": "A",
                        "category_desc": "The Teacher",
                     
                        "average": 4.3
                    },
                    {
                        "category_id": "B",
                        "category_desc": "jkajskashkjA",
                      
                        "average": 4.9
                    },
                    {
                        "category_id": "C",
                        "category_desc": "jkajskashkjA",
                    
                        "average": 2.5
                    },
                    {
                        "category_id": "D",
                        "category_desc": "jkajskashkjA",
                     
                        "average": 3.2
                    },
                    {
                        "category_id": "E",
                        "category_desc": "jkajskashkjA",
                     
                        "average": 4.5
                    },
                ],
               
            },],
        "feedback_summary":[
            {
                "total_feedbacks": 200,
                "total_positive": 50,
                "total_neutral": 50,
                "total_negative": 100,
                "question_summary": [
                    {
                        "feedback_question": 1,
                        "total_feedbacks": 100,
                        "total_positive": 80,
                        "total_neutral": 5,
                        "total_negative": 15,
                    },
                ],
            }
        ],
       "professor_list":[
           {
            "id": 1,
            "name": 'Ronnie Chu',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 4.70,
            "total_feedbacks": 100,
            "total_positive": 80,
            "total_neutral": 5,
            "total_negative": 15,
            },
           {
            "id": 2,
            "name": 'Noreen Perez',
            "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
            "initials": 'RC',
            "total_avg": 4.70,
            "total_feedbacks": 100,
            "total_positive": 70,
            "total_neutral": 15,
            "total_negative": 15,
            },
        ]
            
    },]
        }
        
    ]
        return Response(college_rating, status=status.HTTP_200_OK)

class ProfessorRatingsSummary(APIView):
    def get(self, request):

        professor_ratings_summary = [

        {
            "year_sem": "24-25-1",
            "professors": [{
        "id": "1",
        "name": 'Ronnie Chu',
        "avatarUrl": 'https://i.pinimg.com/564x/da/2a/20/da2a208141d20d42434ef3d4ae9c5d88.jpg',
        "initials": 'RC',
        "dept_id": "CCS",
        "dept_desc": "College of Computer Studies",
        "numerical_summary": [
            {
                "total_avg": 4.7,
                "category_avg": [
                    {
                        "category_id": "A",
                        "category_desc": "The Teacher",
                        "average": 4.5,
                        "question_avg": [
                            {
                                "question_id": "A1",
                                "question_desc": "Articulates course policies, procedures, and grading criteria clearly",
                                "average": 4.6
                            },
                            {
                                "question_id": "A2",
                                "question_desc": "Communicates clearly and utilizes synchronous and asynchronous methods effectively",
                                "average": 4
                            },
                            {
                                "question_id": "A3",
                                "question_desc": "Demonstrates mastery of the subject matter and effectively relates it to other disciplines",
                                "average": 3.2
                            },
                            {
                                "question_id": "A4",
                                "question_desc": "Stimulates the student to think critically",
                                "average": 3
                            },
                            {
                                "question_id": "A5",
                                "question_desc": "Provides timely, constructive feedback to students",
                                "average": 4.2
                            },
                        ],
                    },
                    {
                        "category_id": "B",
                        "category_desc": "The Module/Learning Materials",
                        "average": 3.5,
                        "question_avg": [
                            {
                                "question_id": "B1",
                                "question_desc": "The module/learning materials are clearly structured and well-organized",
                                "average": 4.6
                            },
                            {
                                "question_id": "B2",
                                "question_desc": "The module/learning materials are structured in a logical sequence",
                                "average": 4
                            },
                            {
                                "question_id": "B3",
                                "question_desc": "The module/learning materials provide a balanced representation of the course content",
                                "average": 3
                            },
                            {
                                "question_id": "B4",
                                "question_desc": "The length and difficulty level of the module/learning materials are appropriate",
                                "average": 4
                            },
                            {
                                "question_id": "B5",
                                "question_desc": "The module/learning materials are easily accessible",
                                "average": 2.5
                            },
                        ],
                    },
                    {
                        "category_id": "C",
                        "category_desc": "The Use of LMS",
                        "average": 4.1,
                          "question_avg": [
                            {
                                "question_id": "C1",
                                "question_desc": "The teacher creates and manages classes, assignments, and resources on the LMS effectively",
                                "average": 4.6
                            },
                            {
                                "question_id": "C2",
                                "question_desc": "The teacher adds material to the assignments regularly",
                                "average": 5
                            },
                            {
                                "question_id": "C3",
                                "question_desc": "The teacher uses the LMS to post announcements and updates promptly",
                                "average":3.2
                            },
                            {
                                "question_id": "C4",
                                "question_desc": "The teacher engages students in question-driven discussions using the LMS",
                                "average": 3.5
                            },
                            {
                                "question_id": "C5",
                                "question_desc": "The teacher uses a video conferencing app to conduct synchronous classes effectively",
                                "average": 3
                            },
                        ],
                    },
                    {
                        "category_id": "D",
                        "category_desc": "The Use of Social Media Platforms",
                        "average": 4,
                           "question_avg": [
                            {
                                "question_id": "D1",
                                "question_desc": "The teacher uses the Social Media platform effectively for class activities",
                                "average": 3.9
                            },
                            {
                                "question_id": "D2",
                                "question_desc": "The teacher communicates regularly using the Social Media platform",
                                "average": 3.5
                            },
                            {
                                "question_id": "D3",
                                "question_desc": "The teacher provides opportunities for student interaction on the Social Media platform",
                                "average": 3.5
                            },
                            {
                                "question_id": "D4",
                                "question_desc": "The teacher invites students to post information and resources on the Social Media platform",
                                "average": 3.5
                            },
                            {
                                "question_id": "D5",
                                "question_desc": "The teacher uses the Social Media platform to post important information and updates",
                                "average": 3.5
                            },
                        ],
                    },
                    {
                        "category_id": "E",
                        "category_desc": "General Observation",
                        "average": 3.5,
                          "question_avg": [
                            {
                                "question_id": "E1",
                                "question_desc": "Rapport between teacher and students",
                                "average": 4.2
                            },
                            {
                                "question_id": "E2",
                                "question_desc": "Overall teacher impact",
                                "average": 3
                            },
                        ],
                    },
                    
                ],
                
               
            },],
        "feedback_summary":[
            {
                "total_feedbacks": 100,
                "total_positive": 80,
                "total_neutral": 5,
                "total_negative": 15,
                "question_summary": [
                    {
                        "feedback_question": 1,
                        "total_feedbacks": 100,
                        "total_positive": 80,
                        "total_neutral": 5,
                        "total_negative": 15,
                    },
                ],
            }
        ]
            
    },
    {
            "id": "2",
            "name": 'Noreen Perez',
            "avatarUrl": 'https://cdnb.artstation.com/p/assets/images/images/059/961/409/large/t-o-f-u-tofufaerie-froggo-5105.jpg?1677526327.jpg',
            "initials": 'NP',
            "dept_id": "CCS",
            "dept_desc": "College of Computer Studies",
            "numerical_summary": [
            {
                "total_avg": 4.4,
                "category_avg": [
                    {
                        "category_id": "A",
                        "category_desc": "The Teacher",
                        "average": 4.5,
                        "question_avg": [
                            {
                                "question_id": "A1",
                                "question_desc": "Articulates blablka hsjhsk",
                                "average": 4.6
                            },
                            {
                                "question_id": "A2",
                                "question_desc": "Articulasadasds",
                                "average": 4.6
                            },
                        ],
                    },
                    {
                        "category_id": "B",
                        "category_desc": "jkajskashkjA",
                        "average": 4.9,
                    },
                       {
                        "category_id": "C",
                        "category_desc": "jkajskashkjA",
                        "average": 3.9,
                    },
                    {
                        "category_id": "D",
                        "category_desc": "jkajskashkjA",
                        "average": 3,
                    },
                    {
                        "category_id": "E",
                        "category_desc": "jkajskashkjA",
                        "average": 3.5,
                    },
                ],
                
               
            },],
        "feedback_summary":[
            {
                "total_feedbacks": 100,
                "total_positive": 70,
                "total_neutral": 5,
                "total_negative": 15,
                "question_summary": [
                    {
                        "feedback_question": 1,
                        "total_feedbacks": 100,
                        "total_positive": 80,
                        "total_neutral": 5,
                        "total_negative": 15,
                    },
                ],
            }
        ]
            },
    ]
        }
        
    ]
        return Response(professor_ratings_summary, status=status.HTTP_200_OK)
    
class ProfessorFeedbacks(APIView):
    def get(self, request):

        professor_feedbacks = [

        {
            "year_sem": "24-25-1",
            "professor_feedback_list": [{
            "id": "1",
            "name": "Ronnie Chu",
            "dept_id": "CCS",
            "dept_desc": "College of Computer Studies",
            "feedbacks": [
            {
                "question_id": "1",
      
                "sentiment": "Positive",
                "text": "good teacher"
            },
            {
                "question_id": "2",
          
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "3",
        
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "4",
          
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Negative",
                "text": "boring"
            },
            {
                "question_id": "5",
           
                "sentiment": "Positive",
                "text": "nice"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },


        ]
    
    },]
        },
        {
            "year_sem": "24-25-1",
            "professor_feedback_list": [{
            "id": "2",
            "name": "Noreen Perez",
            "dept_id": "CCS",
            "dept_desc": "College of Computer Studies",
            "feedbacks": [
            {
                "question_id": "1",
              
                "sentiment": "Positive",
                "text": "good teacher siya"
            },
            {
                "question_id": "2",
               
                "sentiment": "Negative",
                "text": "kulang sa time"
            },
            {
                "question_id": "3",
            
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "4",
           
                "sentiment": "Neutral",
                "text": "okay lang"
            },
            {
                "question_id": "5",
            
                "sentiment": "Neutral",
                "text": "okay lang"
            },


        ]
    
    },]
        },
        
    ]
        return Response(professor_feedbacks, status=status.HTTP_200_OK)

class recurringPhrases(APIView):
    def get(self, request):

        recurring_phrases_list = [

        {
            "year_sem": "24-25-1",
            "professor_phrases": [{
            "id": "1",
            "name": "Ronnie Chu",
            "dept_id": "CCS",
            "dept_desc": "College of Computer Studies",
            "recurring_phrases": [
            {
                "count": "8",
                "sentiment": "Positive",
                "phrase": "good teacher"
            },
            {
                "count": "6",
                "sentiment": "Positive",
                "phrase": "magaling magturo"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "6",
                "sentiment": "Positive",
                "phrase": "good teacher"
            },
            {
                "count": "3",
                "sentiment": "Negative",
                "phrase": "laging late"
            },
            {
                "count": "3",
                "sentiment": "Positive",
                "phrase": "kind nice good"
            },
        ]
    
    },]
        },
        {
            "year_sem": "24-25-1",
            "professor_phrases": [{
            "id": "2",
            "name": "Noreen Perez",
            "dept_id": "CCS",
            "dept_desc": "College of Computer Studies",
            "recurring_phrases": [
           {
                "count": "8",
                "sentiment": "Positive",
                "phrase": "good teacher"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
        ]
    
    },]
        },
        
    ]
        return Response(recurring_phrases_list, status=status.HTTP_200_OK)
    

class collegePhrases(APIView):
    def get(self, request):
        recurring_phrases_list = [
        {
            "year_sem": "24-25-1",
            "college_phrases": [{
            "dept_id": "CCS",
            "dept_desc": "College of Computer Studies",
            "recurring_phrases": [
            {
                "count": "8",
                "sentiment": "Positive",
                "phrase": "good teacher"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
            {
                "count": "2",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
        ]
    },]
        },
        {
            "year_sem": "24-25-1",
            "college_phrases": [{
            "id": "2",
            "dept_id": "CAS",
            "dept_desc": "College of Arts and Sciences",
            "recurring_phrases": [
           {
                "count": "8",
                "sentiment": "Positive",
                "phrase": "good teacher"
            },
            {
                "count": "3",
                "sentiment": "Neutral",
                "phrase": "okay lang"
            },
        ]
    
    },]
        },
        
    ]
        return Response(recurring_phrases_list, status=status.HTTP_200_OK)
