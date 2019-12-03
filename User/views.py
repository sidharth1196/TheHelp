from django.shortcuts import render, redirect
from django.http import HttpResponse
from User.models import Worker
from User.forms import UserForm, WorkerForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def workers(request, work_id):
    all_workers = Worker.objects.filter(work__id = work_id)
    return render(request, 'User/services.html', { 'workers' : all_workers })
    
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        worker_form = WorkerForm(data = request.POST)
        user_profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            registered = True
        elif user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            registered = True
        else:
            print(user_form.errors,worker_form.errors)
    else:
        user_form = UserForm()
        worker_form = WorkerForm()
        user_profile_form = UserProfileForm()
    return render(request, 'User/registration.html', {'user_form': user_form, 'worker_form': worker_form, 'user_profile_form': user_profile_form, 'registered': registered })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                #return redirect('/')
                if is_user_profile(user):
                    return HttpResponse("You're a user")
                else:
                    return HttpResponse("You're a worker")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'User/login.html')
        
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
    
def is_user_profile(user_profile):
    if Worker.objects.filter(user__id = user_profile.id).exists():
        return False
    else:
        return True
