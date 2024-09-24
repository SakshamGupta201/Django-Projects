from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from todo.models import Todo
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


@login_required
def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        todo = Todo.objects.create(title=title, user=request.user)
    todos = Todo.objects.all().order_by('-date')
    context = {
        "todos": todos
    }
    return render(request, "todo.html", context)
