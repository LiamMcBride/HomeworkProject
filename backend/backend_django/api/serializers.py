from rest_framework import serializers
from .models import Task, Course

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["task_id", "name", "due_date", "grade", "course"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_id", "name"]        