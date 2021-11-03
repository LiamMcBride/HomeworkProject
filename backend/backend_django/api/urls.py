from django.conf.urls import url
from django.urls import path, include
from .views import TaskApiView, CourseApiView

urlpatterns = [
    path('tasks/', TaskApiView.as_view()),
    path('courses/', CourseApiView.as_view()),
     path('tasks/<str:course_id>', TaskApiView.tasksByCourseId),
]