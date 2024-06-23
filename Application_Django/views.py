from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, age, gender)
        
        if name and age and gender:
            save = Student(name=name, age=age, gender=gender)
            save.save()
            print(name, age, gender)
            return redirect('/') 
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def Delete(request, id):
    if request.method == 'POST':
        id_delete = Student.objects.get(pk=id)
        id_delete.delete()
        return redirect('/')

def Update(request, id):
    if request.method == "POST":
        edit_name = request.POST.get('edit_name')
        edit_age = request.POST.get('edit_age')
        edit_gender = request.POST.get('edit_gender')
        if edit_name and edit_age and edit_gender:
            save = Student(id=id, name=edit_name, age=edit_age, gender=edit_gender)
            save.save()
            return redirect('/')
    return render(request, 'index.html')