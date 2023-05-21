from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user.username, user.email, user.first_name, user.last_name
    ppic = models.ImageField()
    dob = models.DateField()
    gender = models.TextField() #Make it so they can choose only three
    nfollowers = models.IntegerField(default=0)
    nfollowing = models.IntegerField(default=0)
    bio = models.CharField(max_length=10000)
    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    desc = models.TextField()
    pic = models.ImageField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
