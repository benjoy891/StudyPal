from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username,email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')     

    return render(request, 'accounts/login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("login")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect("login")
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, "You are now registered successfully.")
                    return redirect('user_dashboard')
        else:
            messages.error(request, "Password does not match")
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')
    

@login_required(login_url='login')
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'Logged Out')
    return redirect('login')


