from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager,self).get_queryset().filter(city='Hisar')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    discription = models.CharField(max_length=100, default='')
    city = models.CharField(default='',max_length=100)
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.user.username

    Hisar = UserProfileManager()

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)