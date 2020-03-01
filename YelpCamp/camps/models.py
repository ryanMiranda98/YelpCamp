from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Camp(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='camps', null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.resize(output_size)
            img.save(self.image.path)