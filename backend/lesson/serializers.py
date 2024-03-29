from rest_framework import serializers
from .models import *


class ProgressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progression
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    # students_completed = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

        # def create(self, validated_data):
        #     lesson_class = validated_data['lesson_class']

        #     students = lesson_class.students.all()

        #     lesson = Lesson.objects.create(**validated_data)
        #     lesson.students.set(students)
        #     return lesson

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'



class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectAssignmentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    class_assigned = ClassSerializer(read_only=True)

    class Meta:
        model = SubjectAssignment
        fields = '__all__'