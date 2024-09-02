from django.shortcuts import render, get_object_or_404, redirect
from .models import Student  # Import the Student model
from .forms import StudentForm

# students/views.py

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})


def student_list(request):
    students = Student.objects.all()  # Use the Student model here
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

    # students/views.py


# Edit student view
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_detail', student_id=student.id)  # Redirect to the student's detail view or another page
        elif 'delete' in request.POST:
            student.delete()
            return redirect('student_list')  # Redirect to a list of students or another page
    
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# Delete student view (optional, if you want a separate delete confirmation page)
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  # Redirect to a list of students or another page
    return render(request, 'students/delete_student.html', {'student': student})

