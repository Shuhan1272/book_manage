from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from . models import Student
from . forms import StudentForm 

# Create your views here.

def home(request):
    students = Student.objects.all()
    context = {
        "students" : students,
        "search" : False 
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student created successfully!")  # Create message
            return redirect('create')
    form = StudentForm()
    context = {
        "form" : form,
        "create" : True
    }
    return render(request,'create_update.html',context)

def update(request,std_id):
    student = Student.objects.get(id=std_id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.info(request, "Student updated successfully!")  # update message
            return redirect('update', std_id=std_id)
    form = StudentForm(instance=student)
    context = {
        "form" : form,
        "create" : False
    }
    return render(request,'create_update.html',context)

def delete(request,std_id):
    student = Student.objects.get(id=std_id)
    student.delete()
    messages.warning(request, "Student deleted successfully!")  # delete message 
    return redirect('home')

def search_by_name(request):
    name = request.GET['search_by_name'].strip()

    if not name: return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the previous page #on fallback home page

    students = Student.objects.filter(name__contains=name)
    context = {
        "students" : students,
        "searched_name" : name,
        "search" : True
    }
    return render(request,'index.html',context)
