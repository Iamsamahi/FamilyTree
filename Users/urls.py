from django.urls import path
from . import views

urlpatterns = [
    path("" , views.RegistrationView , name ="registration"), 
    
    path("login" , views.LoginView , name ="login"),
    # path("" , views.HomepageView , name ="homepage"),
        
]

