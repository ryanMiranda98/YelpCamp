from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def createProfile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def saveProfile(sender, instance, **kwargs):
#     instance.profile.save()

# Another way of writing signals
# post_save.connect(createProfile, sender=User)