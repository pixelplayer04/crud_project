from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Student, Course
from .forms import StudentForm, CourseForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("student_list")
    else:
        form = AuthenticationForm()
    return render(request, "management/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("student_list")
    else:
        form = UserCreationForm()
    return render(request, "management/register.html", {"form": form})

@login_required
def student_list(request):
    students = Student.objects.all().order_by("first_name")
    form = StudentForm()
    return render(request, "management/student_list.html", {"students": students, "form": form})

@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    return redirect("student_list")

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    return redirect("student_list")

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
    return redirect("student_list")

@login_required
def course_list(request):
    courses = Course.objects.select_related("student").all().order_by("name")
    students = Student.objects.all().order_by("first_name")   # <--- agregado
    form = CourseForm()
    return render(
        request,
        "management/course_list.html",
        {"courses": courses, "students": students, "form": form},
    )

@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    return redirect("course_list")

@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    return redirect("course_list")

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
    return redirect("course_list")