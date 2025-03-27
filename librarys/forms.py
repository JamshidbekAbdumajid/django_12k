from  django import forms
from .models import Course,Lesson,Review

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