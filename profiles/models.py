from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    # user profile model for maintaining default delivery info
    # and order history
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_Truephone_number = models.CharField(max_length=20, null=True, blank=True)
    default_Truecountry = CountryField(blank_label='Country *', null=True, blank=True)
    default_Truepostcode = models.CharField(max_length=20, null=True, blank=True)
    default_Truetown_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_Truestreet_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_Truestreet_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_Truecounty = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create or update user profiles
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save profile
    instance.userprofile.save()