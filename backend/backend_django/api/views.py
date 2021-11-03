from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, Course
from .serializers import TaskSerializer, CourseSerializer
from rest_framework.decorators import api_view
# from dateparser import date_parser
#

class TaskApiView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        maxId = Task.objects.last().task_id + 1
        
        data = {
            'task_id' : maxId,
            'name' : request.data.get('name'),
            'due_date' : request.data.get('due_date'),
            'grade' : request.data.get('grade'),
            'course' : request.data.get('course'),
        }

        

        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(('GET',))
    def tasksByCourseId(request, course_id):
        course = Course.objects.filter(course_id = course_id)
        tasks = Task.objects.filter(course=course[0])
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CourseApiView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        maxId = Course.objects.last().course_id + 1
        
        data = {
            'course_id' : maxId,
            'name' : request.data.get('name'),
            # 'tasks' : request.data.get('tasks'),
        }

        

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    