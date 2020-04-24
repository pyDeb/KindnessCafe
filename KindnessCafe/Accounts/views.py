from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    first_name = ""
    if request.session.has_key('id'):
        first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'index.html', {'first_name' : first_name})



def signup(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect('/signup')
        
        hashed_password = make_password(request.POST.get('password').encode())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
        password=hashed_password, email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        return redirect('/', messages.success(request, 'You were sucessfully singed up!'))

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})



def login_view(request):
    if request.method == "POST":
        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            if (check_password(request.POST['login_password'].encode(), user.password)):
                request.session['id'] = user.id
                return redirect('/', messages.success(request, 'You were successfully logged in!'))


        return redirect('/login', messages.error(request, 'Username and/or password is incorrect'))

    else:
        return render(request, 'login.html')




def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'success.html', context)



def our_mission(request):
    first_name = ""
    if request.session.has_key('id'):
        first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'ourmission.html', {'first_name' : first_name})



def contact_us(request):
    first_name = ""
    if request.session.has_key('id'):
        first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'contact.html', {'first_name' : first_name})


def logout_view(request):
    logout(request)
    return redirect('/', messages.success(request, 'You were successfully logged out!'))


def recruitment_view(request):
    first_name = ""
    if request.session.has_key('id'):
        first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'recruitment.html', {'first_name' : first_name})

