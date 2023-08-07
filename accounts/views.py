from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group, User

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils.crypto import get_random_string
from django.core.mail import BadHeaderError, send_mail
from alphablog.settings import EMAIL_HOST_USER

# Create your views here.
@unauthenticated_user
def Register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            messages.success(request, 'Account was Created for ' + username)
            return redirect('user-login')

    context = {'form':form}
    return render(request, 'register.html', context)
    
@unauthenticated_user
def Login(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog')
            else:
                messages.error(request, "Invalid Credentials")
        except:
                messages.error(request, "Invalid Credentials")

    context = {}
    return render(request, 'login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('user-login')



@login_required(login_url='user-login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST['forgotemail']
        print(email)
        new_password=get_random_string(length=6) #new pswd is generated but not changed yet
        print(new_password)
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Email Not Exists! Please Enter a Valid Email Address')
        user = User.objects.get(email=email)
        
        
        user.set_password(new_password)   #new pswd setting
        user.save()
        send_mail('Reset Password - The MAKEIAS', 'Welcome to The MAKEIAS , Seems like you forgot your password for '+email+ '. Your new password is '+ new_password    +' You can update your desired password in Profile Section , Thanks', EMAIL_HOST_USER, [email])#sending mail
        messages.success(request, 'New Password sended to your Registered Email Address')
        return redirect('user-login')
    return render(request, 'forgotpassword.html')

