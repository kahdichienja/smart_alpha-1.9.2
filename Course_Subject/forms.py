from django import forms
from . models import Subject, SubjectSyllabus, SubjectObjective


class SubjectForm(forms.ModelForm):
    subject_class = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_class', 'required': 'true'}))
    subject_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_name', 'required': 'true'}))
    subject_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_code', 'required': 'true'}))
    subject_start = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'time', 'required': 'true'}))
    subject_duration = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_duration', 'required': 'true'}))
    subject_hod = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_hod', 'required': 'true'}))
    subject_students_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_students_number', 'pattern': '-?[0-9]*(\.[0-9]+)?',  'required': 'true'}))
    subject_details = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_details', 'rows': '4', 'required': 'true'}))
    subject_photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone','id': 'subject_photo', 'accept':'image/*', 'required': 'true'}))
    class Meta:
        model = Subject
        fields = ['subject_name','subject_class','subject_code','subject_hod','subject_details','subject_photo','subject_duration','subject_students_number','subject_start','subject_details']
    
class SubjectSyllabusForm(forms.ModelForm):

    syllabus = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'syllabus', 'rows': '3', 'required': 'true'}))

    class Meta:
        model = SubjectSyllabus
        fields = ['subject','syllabus']

class SubjectObjectiveForm(forms.ModelForm):
    
    objective = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'objective', 'rows': '4', 'required': 'true'}))

    class Meta:
        model = SubjectObjective
        fields = ['subject','objective']