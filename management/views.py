from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm

from django.contrib.auth.decorators import login_required


@login_required
def student_list(request):
    students = Student.objects.all()
    form = StudentForm()

    return render(
        request,
        "management/student_list.html",
        {"students": students, "form": form},
    )


@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect("student_list")


@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

    return redirect("student_list")


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()

    return redirect("student_list")


# ---------------- COURSE ----------------


@login_required
def course_list(request):
    courses = Course.objects.select_related("student")

    form = CourseForm()

    return render(
        request,
        "management/course_list.html",
        {"courses": courses, "form": form},
    )


@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect("course_list")


@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

    return redirect("course_list")


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()

    return redirect("course_list")