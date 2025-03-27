from django.contrib import admin

from .models import Teacher, Student,Payment,Course,Lesson,Enrollment,Review
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Course)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'video')

admin.site.register(Enrollment)
admin.site.register(Review)

