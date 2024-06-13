from django.db import models

def user_directory_path(instance, filename):
    # Set folder based on the field being updated
    if instance._is_cover_photo:
        folder_name = 'coverphotos'
    elif instance._is_profile_photo:
        folder_name = 'profilephotos'
    else:
        folder_name = 'otherphotos'  # This should not happen in this specific case

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
    cover_photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return f'{self.user_name}: {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self._is_cover_photo = bool(self.cover_photo and 'cover_photo' in self.cover_photo.name)
        self._is_profile_photo = bool(self.profile_photo and 'profile_photo' in self.profile_photo.name)
        super().save(*args, **kwargs)
