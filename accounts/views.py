from django.shortcuts import render, redirect # render , renders html template
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)                    #what is going to be a username & password field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, HttpResponse
from django.contrib import messages


# Create your views here.xw
#@login_required() middleware replaces this

def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST': #sending data to web server and receiving
        if form.is_valid():
            form.save()
            messages.success(request, 'User created. You can login now.')
            return redirect(reverse("accounts:login"))
        else:
            pass
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html',args)
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:# accounts for the get
        form = EditProfileForm(instance = request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect('accounts:change_password')
    else:# accounts for the get
        form = PasswordChangeForm(user = request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)