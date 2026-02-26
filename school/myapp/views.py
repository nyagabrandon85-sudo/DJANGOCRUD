from django.shortcuts import render,redirect,get_object_or_404
from . forms import Student
from . forms import StudentForm
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
            return redirect('students')
    return render(request,'studentform.html',{'form':form})
#r-read-fetching all recordings from db
def read_students(request):
    students=Student.objects.all()
    return render(request,'admindashboard.html',{'students':students})
#update updates a record
#delete-deletes a record
def delete_student(request,id):
    student=get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('students')
