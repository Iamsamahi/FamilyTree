from django.urls import path
from . import views 


app_name = 'Site'  # Namespace for URL patterns

urlpatterns = [

    path("" , views.HomepageLoggedInView , name ="homepageLoggedIn"),
    path("logout/",views.custom_logout , name='custom_logout' ),
    path("profile/",views.ProfileView , name='profile' ),
    # path('update_cover_photo/', views.update_cover_photo, name='update_cover_photo'),
    # path('delete_cover_photo/', views.delete_cover_photo, name='delete_cover_photo'),
        
]

