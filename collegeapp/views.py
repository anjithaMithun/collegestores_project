from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import response, HttpResponse
from django.urls import reverse

from collegeapp.forms import RegisterForm, DepartmentCourseForm
from collegeapp.models import Department, Courses, Purpose

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            print("User created successfully!")
            return redirect("collegeapp:login")
        else:
            print("Form is invalid:", form.errors)
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('collegeapp:detail')
        else:
            return HttpResponse("not user")

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')


def department(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})


def courses(request):
    courses = Courses.objects.all()
    print(courses)  # Add this line for debugging
    return render(request, 'department.html', {'courses': courses})


def purpose(request):
    purposes = Purpose.objects.all()
    return render(request, 'index.html', {'purpose': purposes})


from django.shortcuts import render


def submit(request):
    if request.method == 'POST':
        # Process your order logic here

        # Set a message to be passed to the template
        confirmation_message = "Order Confirmed"
        return render(request, 'detail.html', {'confirmation_message': confirmation_message})
    else:
        return render(request, 'index.html')
def your_view(request):
    if request.method == 'POST':
        form = DepartmentCourseForm(request.POST)
        if form.is_valid():
            selected_department = form.cleaned_data['department']
            selected_course = form.cleaned_data['course']
            # Handle form submission or other actions here
    else:
        form = DepartmentCourseForm()

    return render(request, 'detail.html', {'form': form})