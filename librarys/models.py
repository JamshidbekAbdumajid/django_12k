from django.db import models
from django.contrib.auth.models import User  # Django-ning standart User modeli

from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)  # Ism
    last_name = models.CharField(max_length=50)  # Familya
    bio = models.TextField(blank=True)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)  # Ism
    last_name = models.CharField(max_length=50)  # Familya
    grade = models.CharField(max_length=10, blank=True)  # Daraja (A, B, C)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_at = models.DateTimeField(auto_now_add=True)
    


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    payment_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
