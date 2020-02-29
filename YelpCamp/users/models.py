from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    GENDER = [['Male', 'Male'], ['Female', 'Female']]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER)
    profile_img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        user_profile = self.user.username + " Profile"
        return user_profile

    def save(self):
        super().save()
        img = Image.open(self.profile_img.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.resize(output_size)
            img.save(self.profile_img.path)