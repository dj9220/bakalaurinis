from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.
from users.forms import RegisterForm, LoginForm
from django.contrib import messages

def login_page(request):
        forms = LoginForm()
        if request.method == 'POST':
            forms = LoginForm(request.POST)
            if forms.is_valid():
                username = forms.cleaned_data['username']
                password = forms.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('dashboard')
        context = {'form': forms}
        return render(request, 'users/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
@login_required
def profile_page(request):
    user = request.user
    return render(request,'users/Profile-page.html', {'user':user})

