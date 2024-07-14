from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        messages.error(request, 'This is error message.')
    return render(request, 'accounts/signup.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('home')


