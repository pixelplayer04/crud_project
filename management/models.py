from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    enrollment_date = models.DateField()

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    start_date = models.DateField()

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name