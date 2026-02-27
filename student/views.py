from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm


def reg(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            if Student.objects.filter(roll_number=form.cleaned_data['roll_number']).exists():
                form.add_error('roll_number', 'Roll number already exists')
            else:
                Student.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                mobile=form.cleaned_data['mobile'],
                dob=form.cleaned_data['dob'],
                gender=form.cleaned_data['gender'],
                department=form.cleaned_data['department'],
                year=form.cleaned_data['year'],
                roll_number=form.cleaned_data['roll_number'],
                address=form.cleaned_data['address'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],
                skills=", ".join(form.cleaned_data['skills']),
                learning_mode=form.cleaned_data['learning_mode'],
                resume=form.cleaned_data['resume'],
                about=form.cleaned_data['about'],
                agree=form.cleaned_data['agree'],
            )
            return render(request, 'student/base.html')
    else:
        form = StudentForm()

    return render(request, 'student/form.html', {'form': form})