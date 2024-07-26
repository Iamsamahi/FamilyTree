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
        if 'cover_photo' in self.__dict__ and self.cover_photo and self.cover_photo._file:
            self._is_cover_photo = True
        else:
            self._is_cover_photo = False

        if 'profile_photo' in self.__dict__ and self.profile_photo and self.profile_photo._file:
            self._is_profile_photo = True
        else:
            self._is_profile_photo = False
        super().save(*args, **kwargs)
