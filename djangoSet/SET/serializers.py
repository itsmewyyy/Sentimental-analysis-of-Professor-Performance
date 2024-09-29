from rest_framework import serializers
from .models import section, programs, year_level, department

class SectionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='section')

    class Meta:
        model = section
        fields = ['section_id', 'name']


class ProgramSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = programs
        fields = ['program_id', 'program_desc', 'sections']


class YearLevelSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()

    class Meta:
        model = year_level
        fields = ['year_level_id', 'year_level_desc', 'programs']

    def get_programs(self, obj):
        programs_list = programs.objects.filter(sections__year_level=obj).distinct()
        return ProgramSerializer(programs_list, many=True).data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ['department_id', 'department_desc']


class CollegeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='dept_id.department_id')
    description = serializers.CharField(source='dept_id.department_desc')
    years = YearLevelSerializer(many=True, read_only=True)

    class Meta:
        model = programs
        fields = ['name', 'description', 'years']
