from django.shortcuts import redirect
from django.urls import reverse
class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Redirect unauthenticated users trying to access protected pages
        if 'user_name' not in request.session:
            if request.path == reverse('Site:homepageLoggedIn'):
                return redirect('Users:login')
        else:
            # Redirect authenticated users trying to access the registration page
            if request.path == reverse('Users:registration') or request.path == reverse('Users:login'):
                return redirect('Site:homepageLoggedIn')
        response = self.get_response(request)
        return response 
