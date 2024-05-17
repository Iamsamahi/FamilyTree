from django.shortcuts import render

# Create your views here.

def HomepageLoggedInView(request) :
    return render(request ,"Site\HomepageLoggedIn.html")