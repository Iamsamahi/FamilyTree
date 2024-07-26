from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Users.models import Person
from .forms import ProfileForm
import os
from django.conf import settings

@login_required
def HomepageLoggedInView(request):
    user = Person.objects.get(user_name=request.session['user_name'])
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            if 'cover_photo' in request.FILES:
                user.cover_photo = request.FILES['cover_photo']
            if 'profile_photo' in request.FILES:
                user.profile_photo = request.FILES['profile_photo']
            user.save()
            return redirect('Site:homepageLoggedIn')
    else:
        form = ProfileForm(instance=user)

    return render(request, "Site/HomepageLoggedIn.html", {
        "user": user.first_name + ' ' + user.last_name,
        "gender": user.gender,
        "form": form,
        "img_obj": user
    })

@login_required
def ProfileView(request):
    user = Person.objects.get(user_name=request.session['user_name'])
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            if 'cover_photo' in request.FILES:
                user.cover_photo = request.FILES['cover_photo']
            if 'profile_photo' in request.FILES:
                user.profile_photo = request.FILES['profile_photo']
            user.save()
            return redirect('Site:profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, "Site/Profile.html", {
        "user": user.first_name + ' ' + user.last_name,
        "gender": user.gender,
        "form": form,
        "img_obj": user
    })


@login_required
def update_cover_photo(request):
    user = Person.objects.get(user_name=request.session['user_name'])
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('Site:profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, "Site/Profile.html", {
        "user": user.first_name + ' ' + user.last_name,
        "gender": user.gender,
        "form": form,
        "img_obj": user
    })

@login_required
def update_profile_photo(request):
    user = Person.objects.get(user_name=request.session['user_name'])
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  # This will call the save method of the model
            return redirect('Site:profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, "Site/Profile.html", {
        "user": user.first_name + ' ' + user.last_name,
        "gender": user.gender,
        "form": form,
        "img_obj": user
    })


@login_required
def delete_cover_photo(request):
    if request.method == 'POST':
        user = Person.objects.get(user_name=request.session['user_name'])
        if user.cover_photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, user.cover_photo.path))
            user.cover_photo = None
            user.save()
            return redirect('Site:profile')
    return redirect('Site:profile')

def custom_logout(request):
    if 'user_name' in request.session:
        del request.session['user_name']
    return redirect('Users:login')
