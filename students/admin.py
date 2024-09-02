from django.contrib import admin
from .models import Student

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'class_of_student',  'image')  # Customize this as needed
