from django.db import models



class Student(models.Model):
    # first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)

    #date_of_birth = models.DateField()
    #gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
   # religion = models.CharField(max_length=50)
    #nationality = models.CharField(max_length=50)
    #state = models.CharField(max_length=50)
    #address = models.CharField(max_length=255)
    #phone_number = models.CharField(max_length=15)


    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, default='Not Specify', choices=[('Male', 'male'), ('Female', 'female')])
    class_of_student = models.CharField(max_length=50, default='Class 1') 
    
    religion = models.CharField(max_length=50, default='Unknown Religion', choices=[('Islam', 'Islam'), ('Christian', 'Christian')])
    nationality = models.CharField(max_length=50, default='Unknown', choices=[('Nigeria', 'nigeria'), ('Non Nigeria', ('non nigeria'))])
    state = models.CharField(max_length=50, default='Unknown State')
    
    local_government = models.CharField(max_length=100, default='Unknown LGA')
    address = models.CharField(max_length=255, default='Unknown Address')
    phone_number = models.CharField(max_length=15, default='0000000000')
    parent_phone_number = models.CharField(max_length=15, default='0000000000')
     
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




