from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    messages.success(request, 'Account created successfully')
    return render(request, 'registration/register.html', {'form': form})
