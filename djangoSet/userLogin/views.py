from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import student_info, student_acc
from .serializers import StudentAccSerializer
from django.contrib.auth.hashers import check_password

class RegisterView(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = student_info.objects.get(student_id=student_id)
        except student_info.DoesNotExist:
            return Response({'error': 'Student ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        student_acc_data = {'student_acc_number': student_id, 'password': password}
        serializer = StudentAccSerializer(data=student_acc_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student Account registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        student_acc_number = request.data.get('student_acc_number')
        password = request.data.get('password')

        try:
            student_account = student_acc.objects.get(student_acc_number=student_acc_number)
        except student_acc.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, student_account.password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
