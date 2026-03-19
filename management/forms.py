from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "enrollment_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "student": forms.Select(attrs={"class": "form-control"}),
        }