from  django import forms
from .models import Course,Lesson,Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'video', 'order']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment','student','course','rating']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','description','teacher','price']

