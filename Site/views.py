from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required 
from Users.models import Person

# Create your views here.


@login_required
def HomepageLoggedInView(request) :
    user = Person.objects.get(user_name = request.session['user_name'])
    return render(request ,"Site\HomepageLoggedIn.html" , {
        "user" : user.first_name +' '+ user.last_name,
        "gender": user.gender
    })


def custom_logout(request):
    if 'user_name' in request.session:
        del request.session['user_name']
    return redirect('Users:login')