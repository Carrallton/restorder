from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
     OWNER = 1
     PRESS = 2
     WORKER = 3
     first_name = models.CharField("First name", max_length=255)
     last_name = models.CharField("Last name", max_length=255)
     email = models.EmailField(null=True, blank=True, unique=True)
     phone = models.CharField(max_length=20, unique=True)
     description = models.CharField(blank=True, null=True, max_length=255)
     createdAt = models.DateTimeField("Created At", auto_now_add=True)
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = ['first_name', 'last_name']

     def __str__(self):
      return "{}".format(self.email)

class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, default="1")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
