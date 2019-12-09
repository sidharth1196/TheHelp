from django.shortcuts import render, redirect
from django.http import HttpResponse
from User.models import Worker, UserProfile
from WorkOrder.models import Quote, Order
from User.forms import UserForm, WorkerForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

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
                if is_user_profile(user):
                    return redirect('/')
                else:
                    return HttpResponseRedirect('workerprofile/%d' %user.id)
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

def userprofile_info(request, profile_id):
    data = UserProfile.objects.filter(user__id = profile_id)
    quotes = Quote.objects.filter(user_id_id = data[0].id).filter(processed = False)
    orders = Order.objects.filter(user_id = data[0].id)
    return render(request, 'User/userprofile.html', {'data':data[0], 'quotes':quotes, 'orders':orders})

def save_userprofile(request, profile_id):
    if request.method == 'POST':
        data = UserProfile.objects.get(id=profile_id)
        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')
        data.phone = request.POST.get('phone')
        data.address = request.POST.get('address')
        data.save()
    return redirect('/')

def workerprofile(request, userid):
    data = Worker.objects.filter(user__id = userid)
    quotes = Quote.objects.filter(worker_id_id = data[0].id).filter(processed = False)
    orders = Order.objects.filter(worker_id = data[0].id)
    return render(request, 'User/workerprofile.html', {'data':data[0], 'quotes':quotes, 'orders':orders})

def save_workerprofile(request, profile_id):
    if request.method == 'POST':
        data = Worker.objects.get(id=profile_id)
        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')
        data.phone = request.POST.get('phone')
        data.basic_charge = request.POST.get('basic_charge')
        data.save()
    return redirect('/user/user_login/workerprofile/%d' %data.user.id)