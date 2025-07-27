from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class item(models.Model):
    
    def __str__(self):
        return self.item_name      # ---> basicaly teels django that this particular object have this sort of representation 
                                   # --> this method help to show the object name in the python shell
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)   # foreign key establish a connection between User and item model
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    
    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})