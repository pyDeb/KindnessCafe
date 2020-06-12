from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from KindnessCafe.settings import EMAIL_HOST_USER
from django.template import RequestContext
from News.models import News

#imported for email activation
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage




def index(request):
    num_of_news = len(News.objects.all())
    n1_title = ""
    n2_title = ""
    n3_title = ""
    n1_img = ""
    n2_img = ""
    n3_img = ""
    
    if num_of_news > 0:
        n1_title = News.objects.all()[num_of_news - 1].title
        n1_img = News.objects.all()[num_of_news - 1].image_1

    if num_of_news > 1:
        n2_title = News.objects.all()[num_of_news - 2].title
        n2_img = News.objects.all()[num_of_news - 2].image_1

    if num_of_news > 2:
        n3_title = News.objects.all()[num_of_news - 3].title
        n3_img = News.objects.all()[num_of_news - 3].image_1
        
    first_name = ""
    if request.session.has_key('id'):
        if User.objects.filter(id=request.session['id'])[0].is_active:
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'index.html', {'first_name' : first_name, 'num': num_of_news, 'n1_title' : n1_title, 
    'n2_title' : n2_title, 'n3_title' : n3_title, 'n1_img' : n1_img, 'n2_img' : n2_img, 'n3_img' : n3_img})




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
        # request.session['id'] = user.id
        user.is_active = False
        current_site = get_current_site(request)
        mail_subject = 'Activate your KindnessCafe account.'
        message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
        to_email = request.POST['email']
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
            )
        email.send()
        return redirect("/", messages.success(request, 'Please confirm your email to finish signing up'))
        # return redirect('/', messages.success(request, 'You were sucessfully singed up!'))

    else:
        if request.session.has_key('id'):
            return redirect('/')
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        request.session['id'] = uid
        # return redirect('home')
        return redirect("/", messages.success(request, 'Thank you for your email confirmation. Now you are logged in'))
    else:
        return redirect("/", messages.error(request, 'The link is invalid!'))




def login_view(request):
    if request.method == "POST":
        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            if (check_password(request.POST['login_password'].encode(), user.password)):
                request.session['id'] = user.id
                return redirect('/', messages.success(request, 'You were successfully logged in!'))

        return redirect('/login', messages.error(request, 'Username and/or password is incorrect'))

    else:
        if request.session.has_key('id'):
            if User.objects.filter(id=request.session['id'])[0].is_active:
                return redirect('/')
            else:
                return render(request, 'login.html')

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
        if User.objects.filter(id=request.session['id'])[0].is_active:
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'ourmission.html', {'first_name' : first_name})



def contact_us(request):
    if request.method == "GET":
        first_name = ""
        if request.session.has_key('id'):
            if User.objects.filter(id=request.session['id'])[0].is_active:
                first_name = User.objects.filter(id=request.session['id'])[0].first_name
        return render(request, 'contact.html', {'first_name' : first_name})

    else:
        user_email = ""
        if request.session.has_key('id'):
            if User.objects.filter(id=request.session['id'])[0].is_active:
                user_email = User.objects.filter(id=request.session['id'])[0].email
            
        if not user_email:
            user_email = request.POST['email']

        mail_subject = 'Message from ' + user_email
        message =  mail_subject  + '\n' + request.POST['message']
        to_email = EMAIL_HOST_USER + '@gmail.com'
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
            )
        email.send()
        return redirect('/', messages.success(request, 'Your message was sent seccessfully!'))

def logout_view(request):
    logout(request)
    return redirect('/', messages.success(request, 'You were successfully logged out!'))


def recruitment_view(request):
    first_name = ""
    if request.session.has_key('id'):
        if User.objects.filter(id=request.session['id'])[0].is_active:
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'recruitment.html', {'first_name' : first_name})

