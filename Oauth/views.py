from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from . forms import UserRegisterForm, UserLoginForm, TeacherProfileForm
from . models import TeacherProfile
from Department.models import Departments
from Course_Subject.models import Subject

# Create your views here.


def stuff_login(request):
    if request.user.is_authenticated:
        context = {}
        subjects = Subject.objects.all()
        dept_qs = Departments.objects.all()
        context['dept_qs'] = dept_qs
        context['subjects'] = subjects
        
        messages.success(request, f'login was Success!{ request.user.username}')
        return render(request, 'stuff/dashboard.html', context)
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, f'login was Success {username} !!!')
            return redirect('/oauth/')
        else:
            messages.success(
                request, f'login Error !!!! Provide Correct Username And Password')
    else:
        form = UserLoginForm()
        return render(request, 'stuff/login.html', {'form':form})


def stuff_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('/oauth/')  # will change to dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'stuff/register.html', { 'form':form })

def stuff_profile(request):
    context = {}
    # teacherprofile = TeacherProfile.objects.filter(user_id = request.user.id)
    return render(request, 'stuff/profile.html', context)
def all_stuff(request):
    
    teacherprofile = TeacherProfile.objects.all()
    context = {
        'teacherprofile':teacherprofile,
    }
    return render(request, 'stuff/all_stuff.html', context)

def stuff_detail(request, id):
    try:
        profile_detail = TeacherProfile.objects.get(pk=id)

    except ObjectDoesNotExist:
        return render(request, 'stuff/404.html', {})

    context = {
        'profile_detail':profile_detail,
    }
    return render(request, 'stuff/stuff_profile.html', context)


def stuff_create_profile(request):
    context = {}
    departments = Departments.objects.all()
    context['departments'] = departments
    if request.method == 'POST':
        # if request.user.id == request.user.teacherprofile.user_id:
        #     messages.success(request, f'{request.user.teacherprofile.first_name} You Already have A Profile Created Successfully !')
        #     return redirect('/oauth/profile/')
        
        profileform = TeacherProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            obj = profileform.save(commit = False)
            obj.user_id = request.user.id
            obj.save()
            messages.success(request, f'{request.user.teacherprofile.first_name} Created Successfully !')
            return redirect('/oauth/profile/')
        else:
            profileform = TeacherProfileForm()
            context['profileform'] = profileform
            messages.success(request, f'{request.user.username} fill all the fields correctly!')
            return redirect('/oauth/profile/add')
    else:
        profileform = TeacherProfileForm()
        context['profileform'] = profileform
    return render(request, 'stuff/create_teacher_profile.html', context)
@login_required(login_url='/oauth/teachers/')
@staff_member_required(login_url='/oauth/teachers/')
def edit_stuff(request, id):
    context = {}
    teacherprofile_edit = TeacherProfile.objects.get(pk = id)
    context['teacherprofile_edit'] = teacherprofile_edit
    departments = Departments.objects.all()
    context['departments'] = departments
    if request.method == 'POST':  
        TeacherProfile.objects.filter(pk = id).update(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            mobile_number = request.POST['mobile_number'],
            joined_date = request.POST['joined_date'],
            department = request.POST['department'],
            designation = request.POST['designation'],
            gender = request.POST['gender'],
            email = request.POST['email'],
            # profile_photo = request.FILES['profile_photo'],
            dob = request.POST['dob'],
            address = request.POST['address'],
            education = request.POST['education']
        )
        messages.success(request, f'Update Successfully !')
        return redirect('/oauth/profile/')
        
    return render(request, 'stuff/edit_teacher_profile.html', context)


def delete_stuff_profile(request):
    if request.method == 'POST':
        item = request.POST['id']
        deleteprofile = TeacherProfile.objects.get(id=item)
        deleteprofile.delete()
        return redirect('/oauth/teachers/')

def user_loguot(request):
    logout(request)
    messages.success(request, f'You Have logout !!!')
    return redirect('/oauth/')