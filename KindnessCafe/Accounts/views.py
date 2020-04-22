from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from .forms import SignUpForm


def index(request):
    return render(request, 'index.html', {})



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
        return redirect('/', messages.success(request, 'You were singed up successfully!'))

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})



def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        print(user.password)
        print(request.POST['login_password'].encode())
        if (check_password(request.POST['login_password'].encode(), user.password)):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')




def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'success.html', context)



def our_mission(request):
    return render(request, 'ourmission.html', {})



def contact_us(request):
    return render(request, 'contact.html', {})