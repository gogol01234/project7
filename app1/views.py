from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app1.models import Blog
from app1.forms import Edit_Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
def home(request):
    blog = Blog.objects.all()
    context = {"blogs":blog}
    return render(request, "app1/home.html", context)

def about(request):
    return HttpResponse("This is about page.")

def user_register(request):
    if request.method == 'POST':
        fname = request.POST.get("firstname")
        lname = request.POST.get("secondname")
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2:
            messages.warning(request, "Password does not match")
            return redirect("/register/")
        elif User.objects.filter(username = uname).exists():
            messages.warning(request, "Username is already taken")
            return redirect("register")
        elif User.objects.filter(email = email).exists():
            messages.warning(request, "Email is already taken")
            return redirect("register")
        
        else:
            user = User.objects.create_user(first_name = fname,
            last_name = lname, username = uname,email = email, password = pass1)
            user.save()
            messages.success(request, "User has been registered successfully")
            return redirect("login")
    return render(request, "app1/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect("/accounts/login/")

    return render(request, "app1/login.html")

def practice(request):
    return render(request, "app1/practive.html")
def user_logout(request):
    logout(request)
    return redirect("/")

def post_blog(request):
    if request.method == "POST":
        title = request.POST.get("title1") 
        dsc = request.POST.get("description1")
        blog = Blog(title = title, dsc = dsc, user_id = request.user)
        blog.save()
        messages.success(request, "Post  has been submitted successfully.")
        return redirect("/post_blog/")
    return render(request, "app1/post_blog.html")

@login_required
def blog_detail(request, id):
    blog = Blog.objects.get(id = id)
    context = {
        "blog":blog
    }
    return render(request, "app1/blog_detail.html", context)

def delete_post(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    messages.success(request, "Post has been deleted")
    return redirect("/")

def edit(request,id):
    blog = Blog.objects.get(id = id)
    editblog = Edit_Blog(instance = blog)
    if request.method == "POST":
        form = Edit_Blog(request.POST, instance = blog)
        if form.is_valid():
            form.save()
            messages.success(request, "POST has been updated")
            return redirect("/")

    context = {
        "edit_blog":editblog
    }
    return render(request, "app1/Edit_blog.html", context)
