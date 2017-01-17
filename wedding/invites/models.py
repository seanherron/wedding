from django.db import models
from django.conf import settings

from hashids import Hashids

# Create your models here.
class MealOption(models.Model):
    name = models.CharField(max_length=255)

class Invite(models.Model):
    zip_code = models.CharField(max_length=5)
    has_plusone = models.BooleanField(default=False)

    def generate_absolute_url(self):
        hashids = Hashids(salt=settings.HASHIDS_SALT, min_length=settings.HASHIDS_MIN_LENGTH)
        return hashids.encode(self.id)

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    invite = models.ForeignKey(Invite)
    invited_to_family_dinner = models.BooleanField(default=False)
    invited_to_friends_dinner = models.BooleanField(default=False)
    attending_family_dinner = models.NullBooleanField(blank=True, null=True)
    attending_friends_dinner = models.NullBooleanField(blank=True, null=True)
    attending_wedding = models.NullBooleanField(blank=True, null=True)
    meal_choice = models.ForeignKey(MealOption, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
