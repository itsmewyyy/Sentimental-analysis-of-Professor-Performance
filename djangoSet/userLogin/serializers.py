from rest_framework import serializers
from .models import student_info, student_acc, admin_acc
from django.contrib.auth.hashers import make_password

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = '__all__'

class StudentAccSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = student_acc
        fields = ['student_acc_number', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class AdminAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_acc
        fields = '__all__'
