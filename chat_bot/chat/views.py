from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Message
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'chat/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def chat(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        message = Message(user=request.user, content=content)
        message.save()
        return redirect('chat')
    else:
        message = Message.objects.filter(user=request.user).order_by('-timestamp')
        return render(request, 'chat/chat.html', {'messages': message})