from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)#tell django what form to use
        if form.is_valid():#check validity of form
            form.save() #adds user to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account: {username}. Please login and add a Profile Picture!')
            return redirect("tutorial-home")
    else:
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)#request user data 
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,#define forms to use in template
        'p_form': p_form
    }

    return render(request, 'users/update.html', context)