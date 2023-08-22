from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import string, random
from django.contrib.auth.hashers import check_password
from datetime import datetime
from .models import Venue,Book
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as login_details,logout as logout_details
# Create your views here.

def home(request):

    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Confirm_Password = request.POST.get('ConfirmPassword')
        try:
            if User.objects.filter(email = Email).first():
                messages.warning(request, "Email is already exists,please go to signin")
                return redirect('myapp:signup')
            
            if Password != Confirm_Password:
                messages.warning(request, "please check your confirm password")
                return redirect('myapp:signup')
            str_characters = string.ascii_lowercase + string.digits
            username = ''.join(random.choices(str_characters, k=5))  
            user_obj=User(username=First_Name+'_'+username,first_name=First_Name,last_name=Last_Name,email=Email,)
            user_obj.set_password(Password)
            print(user_obj)
            user_obj.save()
            messages.success(request, "sucessfully registered")
            return redirect('myapp:login')
            
        except Exception as e:
            print(e)
    return render(request,'sign-up.html')

def login(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        obj = User.objects.get(email=Email)
        username=obj.username
        print(username)
        user = authenticate(request,email = Email ,password = Password,username=username)
        print(user)
        if user is not None:
            login_details(request, user)
            messages.success(request,f"sucessfully registered {Email}")
            return redirect('myapp:home')
        else:
            messages.warning(request,"login details are incorrect")
            return redirect('myapp:login')
    return render(request,'login.html')
def logout(request):
    logout_details(request)
    messages.success(request,'thank you for spending some moment')
    return redirect('myapp:login')

def venues(request):
    venue_bj=Venue.objects.all()
    contex={
        'venue_bj':venue_bj
    }
    return render(request,'rooms.html',contex)

@login_required(login_url="myapp:login")
def venuebook(request,id):
    venue_obj=Venue.objects.get(vid=id)
    
    if request.method == 'POST':
        
        from_date=request.POST['from_date']
        end_date=request.POST['end_date']
        description=request.POST['description']
        is_available=available(venue_obj,from_date,end_date)
        if is_available:
            Book.objects.create(user=request.user,venue=venue_obj,description=description,from_date=from_date,end_date=end_date,charges=venue_obj.vcharges)
            messages.success(request,f"{request.user}, your booking is sucessfull")
            return redirect('myapp:orders')
        else:
            messages.warning(request,'already booked')

    contex={
        'venue_obj':venue_obj
    }
    return render(request,'room-details.html',contex)

def available(venue,from_date,end_date):
   
    book_obj=Book.objects.filter(
        venue=venue,
        from_date__range=(from_date,end_date)
    )
    return not book_obj

@login_required(login_url="myapp:login")
def order(request):
    contex={
        'book_obj':Book.objects.filter(user=request.user)
    }
    return render(request,'order.html', contex)

@login_required(login_url="myapp:login")
def order_cancle(request, id):
    book_obj = Book.objects.get(bid = id)
    book_obj.status = False
    book_obj.from_date = None
    book_obj.end_date = None
    book_obj.save()

    messages.warning(request, f"{book_obj.venue} cancled successfully")
    return redirect('myapp:orders')

@login_required(login_url="myapp:login")
def change_password(request):
    if request.method == 'POST':
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']
        email = request.POST['email']
        user=User.objects.get(email=email)
        match_password=check_password(old_password,user.password)
        if not match_password:
            messages.warning(request,'old password is not matched')
            return redirect('myapp:Change_password')
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request,'password changed sucessfully')
            return redirect('myapp:Change_password')
    return render(request,'changepassword.html')
