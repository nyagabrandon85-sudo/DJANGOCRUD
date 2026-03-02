from django.shortcuts import render,redirect,get_object_or_404
from . forms import Student
from . forms import StudentForm, RegisterForm
   
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
#create your views here.

# Create your views here.
def index(request):
    return render(request,'index.html')
#crud
#c-create-add a record into db
def create_student(request):
    form=StudentForm(request.POST or None)
    if form.is_valid():
            form.save()
            messages.success(request,'Student created successfully')
            return redirect('students')
    return render(request,'studentform.html',{'form':form})
#r-read-fetching all recordings from db
def read_students(request):
    students=Student.objects.all()
    return render(request,'admindashboard.html',{'students':students})
#update updates a record
def update_student(request,id):
    student=get_object_or_404(Student, pk=id)
    form=StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request,'studentform.html',{'form':form})
#delete-deletes a record
def delete_student(request,id):
    student=get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('students')
#create user
def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User created successfully')
            return redirect('students')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
#login user
def login_user(request):
    if request.method=='POST':
        form=AuthenticationForm( request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if user.is_staff:
                return redirect('students')
        else:        
            return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def user_dashboard(request):
    return render(request,'userdashboard.html')
#logout
def logout_user(request):
    logout(request)
    return redirect('login')
    

