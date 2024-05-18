from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import  login 
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.models import Session 
from .models import Person



# from .models import Registration


def RegistrationView(request):  
    if request.method == "POST":
        # Retrieve data from the form
        user_name = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        dob = request.POST.get('dateField')
        
        # Check if any field is empty
        if not all([user_name, first_name, last_name, email, password1, password2, gender, dob]):
            return render(request, "Users/RegistrationPage.html" , {'general_error' : 'All Fields are required'}) 
        
        # Check if username already exists
        if Person.objects.filter(user_name=user_name).exists():
            return render(request, "Users/RegistrationPage.html", {'user_name_error': "Username already exists."})

        # Check if first name is less than 4 characters
        if len(first_name) <= 4:
            return render(request, "Users/RegistrationPage.html", {'first_name_error': "First name should be more than 4 characters."})

        # Check if passwords match
        if password1 != password2:
            return render(request, "Users/RegistrationPage.html", {'password2_error': "Passwords do not match."})

        # Check if password length is at least 8 characters
        if len(password1) < 8:
            return render(request, "Users/RegistrationPage.html", {'password1_error': "Password should be at least 8 characters."})

        # Check if email already exists in the database
        if email and Person.objects.filter(email=email).exists():
            return render(request, "Users/RegistrationPage.html", {'email_error': "Email already exists."})

        # Create and save the Person object
        person = Person.objects.create(
            user_name=user_name, 
            first_name=first_name,
            last_name=last_name,
            email=email,
            password1=password1,
            password2=password2,
            gender=gender,
            dob=dob
        )
        # Redirect to the login page after successful registration
        return redirect("Users:login")

    return render(request, "Users/RegistrationPage.html")



def custom_authentication(username, password):
    try:
        user = Person.objects.get(user_name=username)
        if user.password1==password: 
            return user  # User authenticated successfully
        else:
            return None  # Incorrect password

    except Person.DoesNotExist:
        return None  # User does not exist
    

def LoginView(request):
    if request.method == "POST":
        username =  request.POST['user_name']
        password =  request.POST['password1']

        user = custom_authentication(username, password)

        if user is not None:
            request.session['user_name']=user.user_name
            return redirect('Site:homepageLoggedIn')  # Redirect to the homepage or any desired page after login

        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, "Users/LoginPage.html", {'error_message': error_message})

    return render(request, "Users/LoginPage.html")

def HomepageView(request) :
    return render(request ,"Users/Homepage.html")