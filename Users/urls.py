from django.urls import path
from . import views

app_name = 'Users'  # Namespace for URL patterns

urlpatterns = [
    path("registration" , views.RegistrationView , name ="registration"), 
    path("login" , views.LoginView , name ="login"),
    path("" , views.HomepageView , name ="homepage"),
        
]

