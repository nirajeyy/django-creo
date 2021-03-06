from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Testers(models.Model):
    user_name = models.CharField(max_length=264,unique=True)
    first_name  =  models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email_id =  models.EmailField(max_length=264,unique=True)
    def __str__(self):
        return self.user_name
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to ='profilepics',default="profilepics/default1.jpg", blank=True)
    def __str__(self):
        return self.user.username
class PostSubmission(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.ImageField(upload_to ='postedpics', blank=True)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,)
    def __str__(self):
        return self.title
