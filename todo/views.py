from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        full_name = request.POST.get('fnm')
        email = request.POST.get("emailid")
        password = request.POST.get("pwd")
        user = User.objects.create_user(
            username=username,
            first_name=full_name,
            email=email
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return redirect('login')


def home(request):
    return render(request, "todo.html")
