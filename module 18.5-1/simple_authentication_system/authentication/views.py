from django.shortcuts import render,redirect
from .forms import RegisterFrom,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def UserRegister(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterFrom(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
        else:
            form = RegisterFrom()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('home')

def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'User login Successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
            
        return render(request,'signin.html',{'form':form})
    else:
        return redirect('home') 


def UserLogout(request):
    logout(request)  
    messages.success(request, 'User logout Successful')
    return redirect('home')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = ChangeUserData(request.POST, instance=request.user)
            changePassForm = PasswordChangeForm(user=request.user,data = request.POST)

            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
            if changePassForm.is_valid():
                changePassForm.save()
                update_session_auth_hash(request= changePassForm.user)
                return redirect('profile')
            
        else:
            form = ChangeUserData(instance=request.user)
            changePassForm = PasswordChangeForm(user=request.user)
        return render(request, 'profile.html', {'form': form,'changePassForm':changePassForm})
    else:
        return redirect('register')


def passwordChange(request):
    form = PasswordChangeForm()
    return render(request,'profile.html',{'form': form})

