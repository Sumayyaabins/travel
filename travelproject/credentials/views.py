from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user=auth.authenticate(username=username1,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    # fetching steps:-
    if request.method == 'POST':
        username1=request.POST['username']
        firstname1 = request.POST['first_name']
        lastname1 = request.POST['last_name']
        mailid1 = request.POST['email']
        password1 = request.POST['password']
        confirm1 = request.POST['confirm password']
        if password1==confirm1:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"username taken")
                return redirect("register")

            elif User.objects.filter(email=mailid1).exists():
                messages.info(request,"email taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username1,password=password1,first_name=firstname1,last_name=lastname1,email=mailid1)

                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect("register")
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
