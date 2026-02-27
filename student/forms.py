from django import forms
from datetime import date
class StudentForm(forms.Form):
    SKILLS = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('Web', 'Web Development'),
    ]

    full_name = forms.CharField(min_length=3)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=10)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female'),('Other','Other')], widget=forms.RadioSelect)

    department = forms.ChoiceField(choices=[('IT','IT'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('MECH','MECH')])
    year = forms.ChoiceField(choices=[('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th')])
    roll_number = forms.CharField()

    address = forms.CharField(widget=forms.Textarea)
    state = forms.ChoiceField(choices=[('AP','Andhra Pradesh'),('TS','Telangana'),('KA','Karnataka'),('TN','Tamil Nadu')])
    pincode = forms.CharField(max_length=6)

    skills = forms.MultipleChoiceField(choices=SKILLS, widget=forms.CheckboxSelectMultiple)
    learning_mode = forms.ChoiceField(choices=[('Online','Online'),('Offline','Offline'),('Hybrid','Hybrid')], widget=forms.RadioSelect)

    resume = forms.FileField()
    about = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile) != 10 or not mobile.isdigit():
            raise forms.ValidationError("Mobile number must be 10 digits")
        return mobile

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob > date.today():
            raise forms.ValidationError("Date of birth cannot be future")
        return dob

    def clean_resume(self):
        resume = self.cleaned_data['resume']
        if not resume.name.endswith(('.pdf','.doc','.docx')):
            raise forms.ValidationError("Only PDF or DOC files allowed")
        return resume