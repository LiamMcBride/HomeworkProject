from django.db import models


 

class Course(models.Model):
    name = models.CharField(max_length=20)
    course_id = models.IntegerField(primary_key=True)
    # tasks = models.ForeignKey()

class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    # task_type = models.ForeignKey(TaskType)
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    # difficulty = models.ForeignKey(Difficulty)   


class TaskType(models.Model):
    name = models.CharField(max_length=10)

class Difficulty():
    name = models.CharField(max_length=10)