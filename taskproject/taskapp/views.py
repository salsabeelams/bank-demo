from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Person
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskapp:login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            cd=loginform.cleaned_data
            user=authenticate(request,username=cd["username"],password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'newform.html')
                else:

                    return HttpResponse("<h2>Disable account</h2>")
            else:
                return HttpResponse("<h2>Invalid login</h2>")
    else:
        loginform=LoginForm()
    return render(request, 'login.html', {'form': loginform})


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account-type')
        print(name,age)
        person = Person(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,district=district,branch=branch,account_type=account_type)
        person.save()
        messages.success(request, 'Form submitted successfully!')

        return redirect('taskapp:submit_form')
    return render(request, 'newform.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('taskapp:home')