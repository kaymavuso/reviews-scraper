from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

import os

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('jobs')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exits')

        # the authenticate method will take in the username and psswors=d and make sure they match
        # will return the user intance or none
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # the login funciton creates a session for the user in the db sessions table/model
            # will also get that session and add it to the browsers cookie
            login(request, user)

            # return redirect('profiles')
            # changing my return to redirect to whatever is passed in as ?next=
            # return redirect(request.GET['next'] if 'next' in request.GET else 'account' )

            return redirect('jobs')

        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'profiles/login_and_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was successfully logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # we could have did form.save here but chose to no commit
            # until we have forced lowercasing the username
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('jobs')

        else:
            messages.warning(request, 'An error has occurred during registration!')


    context = {'page': page, 'form': form}
    return render(request, 'profiles/login_and_register.html', context)

# @login_required(login_url='login')
def userAccount(request):
    # getting the logged in user
    profile = request.user.profile
    jobs = profile.job_set.all()

    context = {'profile': profile, 'jobs': jobs }
    return render(request, 'profiles/account.html', context)

# @login_required(login_url='login')
# def editAccount(request):
#     # getting the logged in user
#     profile = request.user.profile
#     # prefilling form fields
#     form = ProfileForm(instance=profile)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()

#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'users/profile_form.html', context)