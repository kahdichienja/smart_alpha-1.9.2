from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import TeacherProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_email', 'placeholder': 'Email Address', 'required': 'true'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password1','placeholder':'Password', 'required': 'true'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password2','placeholder':'Confirm Password', 'required': 'true'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password', 'placeholder':'Password','required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class TeacherProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'first_name', 'required': 'true'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'last_name', 'required': 'true'}))
    joined_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'date', 'required': 'true'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'id_email', 'required': 'true'}))
    department = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'department','tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    gender = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'gender','tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    designation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'designation', 'required': 'true'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'address', 'required': 'true'}))
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'mobile_number', 'pattern': '-?[0-9]*(\.[0-9]+)?',  'required': 'true'}))
    dob = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'dateOfBirth',  'required': 'true'}))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'address', 'rows': '4', 'required': 'true'}))
    education = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'education', 'rows': '4', 'required': 'true'}))
    profile_photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone','id': 'profile_photo', 'accept':'image/*', 'required': 'true'}))
    class Meta:
        model = TeacherProfile
        fields = ['first_name','last_name','email','mobile_number','profile_photo','joined_date','department','designation','gender','dob','address','education']