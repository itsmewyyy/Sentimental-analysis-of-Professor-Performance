from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import student_acc, admin_acc
from .serializers import StudentAccSerializer
from .serializers import AdminAccSerializer
from django.contrib.auth.hashers import check_password
from datetime import datetime
from SET.models import student_info
from django.contrib.auth import login, logout
from django.contrib.sessions.models import Session

class RegisterView(APIView):
    def post(self, request):

        student_id = request.data.get('student_id')
        student_email = request.data.get('student_email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        dateofbirth = request.data.get('dateofbirth')
        

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = student_info.objects.get(student_id=student_id)
        except student_info.DoesNotExist:
            return Response({'error': 'Student ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)


        if dateofbirth:
            try:
                dateofbirth_parsed = datetime.strptime(dateofbirth, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Use yyyy-mm-dd.'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'Date of birth is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        
        student_acc_data = {
            'student_acc_number': student_id, 
            'password': password, 
            'date_of_birth': dateofbirth_parsed, 
            'plp_email': student_email}
        serializer = StudentAccSerializer(data=student_acc_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student Account registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import login, logout
from django.contrib.sessions.models import Session

class LoginView(APIView):
    def post(self, request):
        student_acc_number = request.data.get('student_acc_number')
        password = request.data.get('password')
        dateofbirth = request.data.get('dateofbirth')

        try:
            student_account = student_acc.objects.get(student_acc_number=student_acc_number)
        except student_acc.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            student_birth = student_acc.objects.get(date_of_birth=dateofbirth)
        except student_acc.DoesNotExist:
            return Response({'error': 'Does not match student date of birth'}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, student_account.password):
            # Create session
            request.session['student_id'] = student_account.student_acc_number
            request.session['user_type'] = 'student'
            
            return Response({
                'message': 'Login successful',
                'student_id': student_account.student_acc_number,
                'user_type': 'student',
            }, status=status.HTTP_200_OK)
           
        return Response({'error': 'Password blasjdklasdhjks'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        if 'student_id' in request.session:
            request.session.flush()  # Removes session data
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Not logged in'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAdmin(APIView):
    def post(self, request):
        username = request.data.get('adminUsername')
        password = request.data.get('password')

        try:
            admin_account = admin_acc.objects.get(admin_username=username)
        except admin_acc.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, admin_account.password):
            # Create session
            request.session['admin_id'] = admin_account.admin_username 
            request.session['user_type'] = 'admin'
           
            
            # Return admin information along with the success message
            return Response({
                'message': 'Login successful',
                'admin_id': admin_account.admin_username,
                'user_type': 'admin',
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAdmin(APIView):
    def post(self, request):
        if 'admin_id' in request.session:
            request.session.flush()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Not logged in'}, status=status.HTTP_400_BAD_REQUEST)

