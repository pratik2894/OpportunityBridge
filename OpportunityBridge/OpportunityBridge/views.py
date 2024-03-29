from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from banner.models import Banner


def SignIn(request):
    if request.method =="POST":
        uname=request.POST['mail']
        pass2 = request.POST['pass']
        user = authenticate(username = uname , password=pass2)
        if user is not None:
            auth_login(request,user)
            fname = user.first_name
            return redirect("home")
        else:
            messages.error(request , "User Enter Invalid Credentials")

    return render(request, "login.html")
def register(request):
    if request.method == "POST":
        username = request.POST['name']
        first = request.POST['fname']
        email = request.POST['email']
        number = request.POST['number']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']

        if User.objects.filter(username=username):
            messages.error(request , "username already Exists!")
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request,"Email is already Exist!")
            return redirect('register')
        if len(number)>10:
            messages.error(request , "invalid Phone number" )
            return redirect('register')
        if len(pass1)<=8:
            messages.error(request , "Password is too short! ")
            return redirect('register')
        if pass1!=pass2:
            messages.error(request,"password Didn't match!")
            return redirect('register')
        myuser = User.objects.create_user(username , email, pass2)
        myuser.first_name = first
        myuser.last_name = number
        myuser.save()
        subject = "Welcome to OpportunityBridge"
        from_email = "shantijadhav116@gmail.com"
        msg  = "<h1> you have succesfully registerd in our site </h1>"
        to = email
        mail = EmailMultiAlternatives(subject,msg,from_email,[to])
        mail.content_subtype='html'
        mail.send()
        messages.success(request,"Account Created Succesfully")
    
        print(username,email,number,pass1,pass2,first)
    return render(request, "register.html")

def Logout(request):
    logout(request)
    return redirect('')

def home(request):
    head=Banner.objects.all()
    head_data={
        'head':head,
    }
    return render(request,"index.html" , head_data)