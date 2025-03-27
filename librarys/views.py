from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import ReviewForm,CourseForm,LessonForm
from  .models import Course,Lesson,Payment,Review,Enrollment,Teacher
# def user_view(request):
#     username ="Hello Django"
#     return HttpResponse(f" {username}")



def home_redirect(request):
    return redirect('course-list')
def welcome_view(request):
    return render(request, 'library/home.html')  # Foydalanuvchiga welcome sahifa ko‘rsatiladi

# ================================================


def courses_list(request):
    return render(request, 'library/courses_listem.html')

def teachers_list(request):
    return render(request, 'library/teacher_listem.html')

def add_course(request):
    return render(request, 'library/add_courses.html')

def add_lesson(request):
    return render(request, 'library/add_lesson.html')

def review_page(request):
    return render(request, 'library/review_listem.html')



















# ==========================================Teacher======================================================================
def teacher_view(request):
    search = request.GET.get('search')
    if search:

        forms = Teacher.objects.filter(first_name__icontains=search)
    else:
        forms = Teacher.objects.all()
    return render(request,'library/teacher.html',{'forms':forms, "search":search})


def teacher_list(request,pk):
    forms = Teacher.objects.get(pk=pk)
    return render(request,'library/teacher_list.html',{'forms':forms})



# ===============================================Courses===================================================





def courses_view(request,pk):
    forms = Course.objects.get(pk=pk)
    return render(request, 'library/course.html', {'forms':forms})

def course_list(request):
    search = request.GET.get('search')
    if search:
        forms = Course.objects.filter(title__icontains=search)
    else:
        forms = Course.objects.all()
    return render(request,'library/courses_lis.html',{'forms':forms,"search":search})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return  redirect('course-list')
    else:
        form = CourseForm()
    return render(request, 'library/create_curs.html', {'form':form})






# ==========================================================Lesson================================================




def lessons_view(request,pk):
    forms = Lesson.objects.get(pk=pk)
    return render(request,'library/lesson_view.html',{'forms':forms})



def lesson_list(request):
    search = request.GET.get('search')
    if search:
        forms = Lesson.objects.filter(title__icontains=search)
    else:
        forms = Lesson.objects.all()
    return  render(request,'library/lesson_list.html',{'forms':forms,"search":search})



def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            return redirect('lesson-list')
    else:
        form = LessonForm()
    return render(request,'library/lesson.html',{'form':form})









# ==============================================Review======================================

def review_view(request,pk):
    forms = Review.objects.get(pk=pk)
    return render(request,'library/review_view.html',{'forms':forms})

def review_list(request):

    forms = Review.objects.all()
    return render(request,'library/review_list.html',{'forms':forms})




def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-review')
    else:
        form = ReviewForm()
    return  render(request,'library/create_review.html',{'form':form})






