from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from Oauth.models import TeacherProfile
from . forms import DepartmentsForm
from . models import Departments

# Create your views here.

def all_department(request):
    
    departments = Departments.objects.all()
    context = {
        'departments':departments,
    }
    return render(request, 'dept/all_department.html', context)


def create_department(request):
    context = {}
    teacherprofile = TeacherProfile.objects.all()
    context['teacherprofile'] = teacherprofile
    if request.method == 'POST':        
        deptform = DepartmentsForm(request.POST)
        if deptform.is_valid():
            obj = deptform.save(commit = False)
            obj.head_of_department_id = request.POST['hod']
            obj.save()
            messages.success(request, f'Department Created Successfully !')
            return redirect('/dept/departments/')
        else:
            deptform = DepartmentsForm()
            context['deptform'] = deptform
            messages.success(request, f'{request.user.username} fill all the fields correctly!')
            return redirect('/dept/departments/add/')
    else:
        deptform = DepartmentsForm()
        context['deptform'] = deptform
    return render(request, 'dept/create_department.html', context)

def edit_department(request, id):
    context = {}
    teacherprofile = TeacherProfile.objects.all()
    context['teacherprofile'] = teacherprofile
    dept_edit = Departments.objects.get(pk=id)

    context['dept_edit'] = dept_edit
    if request.method == 'POST':
        Departments.objects.filter(pk = id).update(
            student_capacity = request.POST['student_capacity'],
            department_name = request.POST['department_name'],
            head_of_department_id = request.POST['hod'],
            starting_year = request.POST['starting_year'],
            department_details = request.POST['department_details']
        )
        messages.success(request, f'Update Successfully !')
        return redirect('/dept/departments/')

    return render(request, 'dept/edit.html', context)

def delete_department(request):
    if request.method == 'POST':
        item = request.POST['id']
        deletedept = Departments.objects.get(id=item)
        deletedept.delete()
        messages.success(request, f'Department Deleted Successfully !')
        return redirect('/dept/departments/')
