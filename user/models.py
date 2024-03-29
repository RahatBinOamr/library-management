from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField( upload_to='profile_images',default='default.png',)
    bio = models.TextField()
    borrowing_book = models.PositiveSmallIntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.user.username
    

