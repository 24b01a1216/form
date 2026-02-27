from django.db import models
class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    DEPT_CHOICES = [
        ('IT', 'IT'),
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('MECH', 'MECH'),
    ]
    YEAR_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    ]
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('TS', 'Telangana'),
        ('KA', 'Karnataka'),
        ('TN', 'Tamil Nadu'),
    ]
    LEARNING_MODE = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    department = models.CharField(max_length=10, choices=DEPT_CHOICES)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    roll_number = models.CharField(max_length=20, unique=True)

    address = models.TextField()
    state = models.CharField(max_length=5, choices=STATE_CHOICES)
    pincode = models.CharField(max_length=6)

    skills = models.CharField(max_length=200)
    learning_mode = models.CharField(max_length=10, choices=LEARNING_MODE)

    resume = models.FileField(upload_to='resumes/')
    about = models.TextField()
    agree = models.BooleanField()

    def __str__(self):
        return self.full_name
