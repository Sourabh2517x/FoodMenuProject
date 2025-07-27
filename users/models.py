from django.db import models
from django.contrib.auth.models import User           # --> User is inbuilt model of django

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)          # --> on delete there will be no profile of user stored 
    image = models.ImageField(default='profilepictures/profilepic.jpg',upload_to='profilepictures')
    location = models.CharField(max_length=100)
    
    def __str__(self):                                             # --> help to access objects in the model
        return self.user.username
    
