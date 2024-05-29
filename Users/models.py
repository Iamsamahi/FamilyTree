from django.db import models
import os

def user_directory_path(instance, filename):
    # Determine whether it's a cover photo or profile photo
    if instance.cover_photo:
        folder_name = 'coverphotos'
    elif instance.profile_photo:
        folder_name = 'profilephotos'
    else:
        folder_name = 'otherphotos'  # You can handle other types of photos as needed

    # File will be uploaded to MEDIA_ROOT/user_<id>/<folder_name>/<filename>
    return f'{instance.user_name}/{folder_name}/{filename}'

class Person(models.Model):
    user_name = models.CharField(max_length=125, unique=True, primary_key=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    cover_photo = models.ImageField(upload_to=user_directory_path, null=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return f'{self.user_name}: {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        # Check if the user has uploaded the first cover photo
        if self.cover_photo and not hasattr(self, '_cover_photo'):
            # Create directory if it doesn't exist
            directory = os.path.join('media', user_directory_path(self, ''))
            if not os.path.exists(directory):
                os.makedirs(directory)
            self._cover_photo = True  # Set a flag to indicate that cover photo is uploaded

        # Check if the user has uploaded the first profile photo
        if self.profile_photo and not hasattr(self, '_profile_photo'):
            # Create directory if it doesn't exist
            directory = os.path.join('media', user_directory_path(self, ''))
            if not os.path.exists(directory):
                os.makedirs(directory)
            self._profile_photo = True  # Set a flag to indicate that profile photo is uploaded

        super().save(*args, **kwargs)
