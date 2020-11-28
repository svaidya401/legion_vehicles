from django.shortcuts import render
from user_app.forms import UserForm, UserProfileForm
from user_app.models import Role, UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            role = Role.objects.get(name='EVERYONE')
            profile.role = role

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES('profile_pic')

            profile.save()
            registered = True

        else:
            print("ERROR : {} {}".format(user_form.errors, profile_form.errors))

    else :
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'user_app/registration.html',
                  { 'user_form' : user_form,
                    'profile_form':profile_form,
                    'registered':registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('bikes_app:bikesHome'))

            else:
                return HttpResponse('Account not Active')

        else:
            print("INVALID CREDENTIALS : Username- {} and password- {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")

    else:
        return render(request, 'user_app/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('bikes_app:bikesHome'))

@login_required
def user_info(request):
    print("LOGGED IN USER : {}".format(request.user.username))
    logged_in_user = request.user.username
    user = User.objects.get(username=logged_in_user)
    profile = UserProfile.objects.get(user=user)
    return render(request, "user_app/user_info.html", {"user_profile":profile})
