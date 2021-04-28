from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .models import Profile, Message

# Create your views here.
from users.forms import RegisterForm, LoginForm, MessageForm
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
    profile = Profile.objects.filter(user=request.user)
    return render(request,'users/Profile-page.html', {'profile':profile})

@login_required
def write_message(request):
    user = Message.objects.filter(sender=request.user)
    if request.method=='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MessageForm()

    return render(request,'users/send-message.html', {'form':form, 'sender':user})
@login_required
def get_inbox(request):
    msg = Message.objects.all()
    return render(request, 'users/inbox.html', {'msg':msg})
def succes(request):
    return render(request,'users/succes.html',{})

class SendMessageView(View):
    def post(self, request, *args, **kwargs):
        reciever_id = request.POST.get('reciever_id','')
        message = request.POST.get('message','')
        Message.objects.create(sender=request.user, reciever__id=reciever_id,message_content=message)
        return render(request, 'users/send-message.html', {})