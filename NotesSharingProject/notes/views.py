from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Signup  # Import your Signup model here
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Notes  # Ensure this line is present
from django.contrib.auth.decorators import login_required



# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST.get('emailid')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_admin.html', d)

def signup1(request):
    error = ""
    if request.method == "POST":
        f = request.POST.get('firstname')
        l = request.POST.get('lastname')
        c = request.POST.get('contact')
        e = request.POST.get('emailid')
        p = request.POST.get('password')
        b = request.POST.get('branch')
        r = request.POST.get('role')
        try:
            user = User.objects.create_user(username=e, password=p, first_name=f, last_name=l)
            sign = Signup.objects.create(user=user, contact=c, branch=b, role=r)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'signup.html', d)

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request, 'admin_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated
    user_instance = request.user  # Fetch the current authenticated user
    try:
        signup_instance = Signup.objects.get(user=user_instance)
    except Signup.DoesNotExist:
        signup_instance = None  # Handle the case where Signup object doesn't exist for the user

    d = {'data': signup_instance, 'user': user_instance}
    return render(request, 'profile.html', d)

def changepassword(request):
    error = ""  # Initialize the error variable
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']

        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'changepassword.html', d)


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated

    user_instance = request.user  # Fetch the current authenticated user
    try:
        signup_instance = Signup.objects.get(user=user_instance)
    except Signup.DoesNotExist:
        signup_instance = None  # Handle the case where Signup object doesn't exist for the user

    error = None

    if request.method == 'POST':
        f = request.POST.get('firstname')
        l = request.POST.get('lastname')
        c = request.POST.get('contact')
        b = request.POST.get('branch')

        user_instance.first_name = f
        user_instance.last_name = l
        user_instance.save()

        if signup_instance:  # Ensure signup_instance is not None before accessing its attributes
            signup_instance.contact = c
            signup_instance.branch = b
            signup_instance.save()

        error = True

    d = {'data': signup_instance, 'user': user_instance, 'error': error}
    return render(request, 'edit_profile.html', d)

def upload_notes(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        subject = request.POST.get('subject')
        notes_file = request.FILES.get('notesfile')
        filetype = request.POST.get('filetype')
        description = request.POST.get('description')

        if not branch or not subject or not notes_file or not filetype:
            return render(request, 'upload_notes.html', {'error': 'yes'})

        # Process and save the uploaded file and form data as needed
        # ...

        return render(request, 'upload_notes.html', {'error': 'no'})
    return render(request, 'upload_notes.html')

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    notes=Notes.objects.filter(user=user)


    d = {'notes':notes}
    return render(request,'view_mynotes.html',d)

def view_users(request):
    if  not request.user.is_authenticated:
        return redirect('login_admin')
    users = Signup.objects.all()
    d = {'users':users}
    return render(request,'view_users.html',d)

def delete_users(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

def pending_notes(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status = "pending")
    d = {'notes' : notes}
    return render(request,'pending_nottes.html',d)





