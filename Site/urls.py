from django.urls import path
from . import views 


app_name = 'Site'  # Namespace for URL patterns

urlpatterns = [

    path("" , views.HomepageLoggedInView , name ="homepageLoggedIn"),
        
]

