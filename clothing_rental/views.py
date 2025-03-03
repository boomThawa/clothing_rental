from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def shop_detail(request):
    return render(request, "shop_detail.html")

def shop_listing(request):
    return render(request, "shop_listing.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("index")  # เปลี่ยนไปหน้า home หรือหน้าหลักหลังจาก login
        else:
            messages.error(request, "Invalid email or password")
    
    return render(request, "auth.html")  # ใช้ auth.html แทน login.html

def home(request):
    return render(request, 'index.html', {
        'user': request.user,
    })

def user_signup(request):
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")

    return render(request, "auth.html")  # ใช้ auth.html แทน signup.html

def user_logout(request):
    logout(request)
    return redirect("login")  # กลับไปหน้า login
