from django import forms
from .models import Student

#class StudentForm(forms.ModelForm):
 #   class Meta:
  #      model = Student
   #     fields = ['first_name', 'last_name', 'date_of_birth', 'gender',  'image']
        

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image',
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'religion', 'state', 'local_government', 
            'nationality', 'address', 'phone_number', 
            'parent_phone_number', 'class_of_student' 
        ]

