from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user.forms import RegisterForm, LoginForm
from user.models import Profile


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == "POST":
        form = RegisterForm()
        if not form.is_valid():
            return render(request,'user/register.html', {'form': form})
        User.objects.crete_user(
            username = form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            password=form.cleaned_data['password']
        )
        user = authenticate(username=form.cleaned_data["username"], password = form.cleaned_data["password"])
        login(request, user)
        return redirect('main')


def login_view(request):
    if request.method =="GET":
        form = LoginForm()
        return render(request, "user/login.html", {'form':form})
    if  request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', {'from':form})

        user = authenticate(
            **form.cleaned_data
        )
        if not user:
            form.add_error(None, "Пользователь не найден ")
            return render(request, 'user/login.html', {'form': form})

        login(request, user)
        return redirect('main')


@login_required(login_url="login")
def logout_view(request):
    logout(request)

    return redirect('main')


@login_required(login_url="login")
def profile_view(request):
    return render(request, 'user/profile.html')

def profiles_view(request):
    if request.method == "GET":
        profiles = Profile.objects.all()
        return render(request, 'user/profiles_list.html', {'profiles': profiles})


def profile_detail_view(request, profile_id):
    if request.method == "GET":
        profile = Profile.objects.get(id=profile_id)
        return render(request, "user/profile_detail.html", {"profile": profile})#"user/user_detail.html"
