from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm

def studentFormView(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            stud_create=StudentModel.objects.create(name=name,email=email,password=password,create_at="",updated_at="")
            stud_create.save()
            fm=StudentForm()
    else:
        fm=StudentForm()
    return render(request,'reg.html',{'fm':fm})
 