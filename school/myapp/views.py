from django.shortcuts import render

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
            return render(request,'index.html')
    return render(request,'studentform.html',{'form':form})