from  django.urls import  path
from  .views import (teacher_view,teacher_list,create_course,course_list,
                     courses_view,create_lesson,lessons_view,lesson_list,
                     create_review,review_view,review_list,home_redirect,welcome_view,
                     course_list,teacher_list,add_course,add_lesson,review_page)

urlpatterns = [
    # path('user/',user_view,name='user'),
    path('', welcome_view, name='welcome'),
    path('', home_redirect, name='home'),


    path('',course_list,name='course-list'),
    path('',teacher_list,name='teacher-list'),
    path('',add_course,name='create-course'),
    path('',add_lesson,name='create-lesson'),
    path('',review_page,name='review-list'),


    # ==============Teacher===============
    path('teacher/',teacher_view,name='teacher'),
    path('teacher/list/<int:pk>/',teacher_list,name='teacher-list'),

    # ==============Courses=========================
    path('courses/list/', course_list, name='course-list'),
    path('courses/',create_course,name='create-course'),
    path('courses/<int:pk>/',courses_view,name='course-view'),

    # =====================LESSONS===================

    path('lessons/',create_lesson,name='create-lesson'),
    path('lessons/view/<int:pk>/',lessons_view,name='lesson-view'),
    path('lessons/list/',lesson_list,name='lesson-list'),

    # =============================REVIEW========================

    path('review/',create_review,name='create-review'),
    path('review/view/<int:pk>/',review_view,name='review-view'),
    path('review/list/',review_list,name='review-list'),

]
