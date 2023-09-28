from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from collegeapp.models import Department,Courses


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # You can add more fields here


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
# forms.py



class DepartmentCourseForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="-- Select Department --",
        required=False
    )
    course = forms.ModelChoiceField(
        queryset=Courses.objects.none(),
        empty_label="-- Select Course --",
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Courses.objects.none()
