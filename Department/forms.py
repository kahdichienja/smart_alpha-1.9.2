from django import forms
from . models import Departments


class DepartmentsForm(forms.ModelForm):
    department_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'department_name', 'required': 'true'}))
    starting_year = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'date', 'required': 'true'}))
    student_capacity = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'student_capacity', 'pattern': '-?[0-9]*(\.[0-9]+)?',  'required': 'true'}))
    department_details = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'department_details', 'rows': '4', 'required': 'true'}))
    class Meta:
        model = Departments
        fields = ['department_name','starting_year','student_capacity','department_details']