from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
    else:
        return redirect('login')  # ou une autre vue appropriée

    return render(request, 'userprofile/profile.html', {'profile': user_profile})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:  # vérifie si l'utilisateur est authentifié
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('profile')
            else:
                return redirect('login')  # redirige vers la page de connexion si l'utilisateur n'est pas authentifié
    else:
        form = UserProfileForm()
    return render(request, 'userprofile/create_profile.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'userprofile/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('change_password_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userprofile/change_password.html', {'form': form})