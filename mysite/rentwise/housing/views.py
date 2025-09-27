from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'housing/home.html')

def properties(request):
    return render(request, 'housing/properties.html')

def details(request, id):
    return render(request, 'housing/details.html', {'id': id})

def about(request):
    return render(request, 'housing/about.html')

def contact(request):
    return render(request, 'housing/contact.html')

def login_view(request):
    return render(request, 'housing/login.html')

def register_view(request):
    return render(request, 'housing/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'housing/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "✅ Login successful!")
            return redirect('home')
        else:
            messages.error(request, "❌ Invalid username or password!")

    return render(request, 'housing/login.html')
