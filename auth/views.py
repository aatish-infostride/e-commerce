

from django.contrib import messages
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from ecom import settings
from django.conf import settings
from auth.models import CustomUser
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from ecom.settings import EMAIL_HOST_USER
from django.contrib.auth.hashers import check_password






# Create your views here.

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def signup(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password==confirm_password:

                if CustomUser.objects.filter(email=email, name = name).exists():
                    messages.info(request, 'account already exists',extra_tags='both' )
                    return redirect('signup')

                elif CustomUser.objects.filter(name=name).exists():
                    messages.info(request, 'Username is already taken',extra_tags='username')
                    return redirect('signup')

                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email is already taken',extra_tags='email' )
                    return redirect('signup')
                
                else:
                    user = CustomUser.objects.create_user(name=name,email=email, password=password)
            
                    user.save()
                    
                    return redirect('/auth/login')

            else:
                messages.info(request, 'Both passwords are not matching', extra_tags='password')
                return redirect('signup')
            
        return render(request, '_templates/pages/auth/signup.html')


        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember_me')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            if remember:
                request.session.set_expiry(60*60)
            return redirect('/store/dashboard')
        else:
            messages.info(request, 'Invalid Username or Password' , extra_tags='invalid')
            return redirect('login')
    
    return render(request, '_templates/pages/auth/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')



def account(request,id):
    current_user = request.user
    CustomUser.objects.get(id=id)
    print (current_user.id)
    return render(request, '_templates/pages/auth/account-settings.html', {'current_user':current_user})


def updaterecord(request, id):
    current_user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        image = request.POST.get('myfile')
        print(name)
        member = CustomUser.objects.get(id=id)

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'email already exists', extra_tags='email')
            return render(request, '_templates/pages/auth/account-settings.html',{'current_user':current_user})

        else:
            member.name = name
            print(member.name)
            member.email = email
            member.image = image
            member.save()

            return redirect('dashboard')
        
    else:
        
        return render(request, '_templates/pages/auth/account-settings.html',{'current_user':current_user})




def forgot_view(request):
    if request.method == "POST":
        email = request.POST.get('email')

        associated_users = CustomUser.objects.filter(email=email)

        if associated_users.exists():

            subject='A cool subject',
            message='A stunning message',
            from_email=settings.EMAIL_HOST_USER,
            print(from_email)
            recipient_list=[email]
            print(recipient_list)

            try:

                email = EmailMessage(subject, message)
                email.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            return render(request, '_templates/pages/auth/success.html', {'recepient': recipient_list})

        else:
            messages.info(request, 'account does not exist' , extra_tags='forgot')
            return redirect('forgot')
            
    return render(request, '_templates/pages/auth/forgot-password.html')


def change_password(request,id):
    current_user= request.user
    if request.method=='POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        u = CustomUser.objects.get(id=id)
        u.set_password(new_password)
        u.save()

        return redirect('dashboard')

    return render(request, '_templates/pages/auth/change-password.html',{'current_user':current_user})