from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from Eauction.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        Contact = contact(name=name, email=email, phone=phone, msg=msg)
        Contact.save()
    return render(request, 'base.html')

def reg(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password & confirm password are not the same.")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('loginpage')

    return render(request, 'reg.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!")

    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

def addproduct(request):
    return render(request, 'addproduct.html')

def final(request, pk):
    prod = get_object_or_404(image, id=pk)

    if request.method == "POST":
        caption = request.POST.get("caption")
        des = request.POST.get("des")
        price = request.POST.get("price")
        email = request.POST.get("email")
        record = orderlist(caption=caption, des=des, price=price, email=email)
        record.save()

        send_mail(
            'E-Auction Bid Confirmation',
            f'Hello {email}, you placed a bid on "{caption}" with price ₹{price}. We will notify if it’s the highest.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        return redirect('final', pk=pk)

    bids = orderlist.objects.filter(caption=prod.caption)
    all_bids = orderlist.objects.all()
    highest_bid = bids.order_by('-price').first() if bids.exists() else None

    context = {
        'prod': prod,
        'bids': bids,
        'showdata': all_bids,
        'highest_bid': highest_bid
    }

    return render(request, 'final.html', context)

def showall(request):
    showdata = orderlist.objects.all()
    display = {'showdata': showdata}
    return render(request, "final.html", display)

def bidpage(request):
    products = image.objects.all()
    return render(request, 'bid.html', {'products': products})