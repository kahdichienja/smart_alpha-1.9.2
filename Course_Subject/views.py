from django.shortcuts import render, redirect
from django.contrib import messages
from Department.models import Departments
from . forms import SubjectForm, SubjectSyllabusForm, SubjectObjectiveForm
from . models import Subject, SubjectSyllabus, SubjectObjective
# Create your views here.
def all_subject(request):
    context = {}
    subjects = Subject.objects.all()
    context['subjects'] = subjects

    return render(request, 'subject/all_subject.html', context)


def add_subject(request):
    context = {}
    hods = Departments.objects.all()
    context['hods'] = hods

    if request.method == 'POST':
        subjectform = SubjectForm(request.POST, request.FILES)
        if subjectform.is_valid():
            obj = subjectform.save(commit = False)
            obj.subject_hod = request.POST['subject_hod']
            obj.subject_class = request.POST['subject_class']
            obj.save()
            messages.success(request, f'Subject Added Successfully !')
            return redirect('/subject/add/')
    else:
        subjectform = SubjectForm()
        context['subjectform'] = subjectform
    return render(request, 'subject/add_subject.html', context)

def subject_detail(request, id):
    context = {}
    subject = Subject.objects.get(pk = id)
    syllabus_qs = SubjectSyllabus.objects.filter(subject_id = id)
    objective_qs = SubjectObjective.objects.filter(subject_id = id)
    context['subject'] = subject
    context['syllabus_qs'] = syllabus_qs
    context['objective_qs'] = objective_qs


    if request.method == 'POST':
        syllabusform = SubjectSyllabusForm(request.POST)
        objectiveform = SubjectObjectiveForm(request.POST)
        if syllabusform.is_valid():
            uri_id = request.POST['subject']
            obj = syllabusform.save(commit = False)
            obj.subject_id = request.POST['subject']
            obj.save()
            return redirect(f'/subject/subject/{uri_id}/')

        elif objectiveform.is_valid():
            uri_id = request.POST['subject']
            obj = objectiveform.save(commit = False)
            obj.subject_id = request.POST['subject']
            obj.save()
            return redirect(f'/subject/subject/{uri_id}/')

    else:
        syllabusform = SubjectSyllabusForm()
        objectiveform = SubjectObjectiveForm()
        context['syllabusform'] = syllabusform
        context['objectiveform'] = objectiveform

    return render(request, 'subject/subject_detail.html', context)

