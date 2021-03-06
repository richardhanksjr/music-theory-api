from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    premium_user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}, {self.user.email}, {self.user.userprofile.premium_user}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # pylint: disable=unused-argument
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # pylint: disable=unused-argument
    instance.userprofile.save()