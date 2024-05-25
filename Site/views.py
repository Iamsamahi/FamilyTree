from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required 
from Users.models import Person
from .forms import ProfileForm
import os
from django.conf import settings

# Create your views here.


@login_required
def HomepageLoggedInView(request) :
    user = Person.objects.get(user_name = request.session['user_name'])
    return render(request ,"Site\HomepageLoggedIn.html" , {
        "user" : user.first_name +' '+ user.last_name,
        "gender": user.gender
    })


def ProfileView(request):
    user = Person.objects.get(user_name=request.session['user_name'])
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('Site:profile')  # Assuming you have a URL named 'profile'
    else:
        form = ProfileForm(instance=user)

    return render(request, "Site/Profile.html", {
        "user": user.first_name + ' ' + user.last_name,
        "gender": user.gender,
        "form": form,
        "img_obj": user
    })


def custom_logout(request):
    if 'user_name' in request.session:
        del request.session['user_name']
    return redirect('Users:login')