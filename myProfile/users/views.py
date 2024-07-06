# users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from .models import UserProfile

@login_required
def home(request):
    return render(request, 'users/home.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    if user.userprofile.public_access:
        return render(request, 'users/public_profile.html', {'user': user})
    else:
        return render(request, 'users/no_access.html')

def all_profiles(request):
    profiles = UserProfile.objects.filter(public_access=True)
    return render(request, 'users/all_profiles.html', {'profiles': profiles})
