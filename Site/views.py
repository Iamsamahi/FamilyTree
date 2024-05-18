from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required 

# Create your views here.


@login_required
def HomepageLoggedInView(request) :
    return render(request ,"Site\HomepageLoggedIn.html")


def custom_logout(request):
    if 'user_name' in request.session:
        del request.session['user_name']
    return redirect('Users:login')