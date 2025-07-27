from django.db.models.signals import post_save       # post_save is a signal sent during the form.save in register view
from django.contrib.auth.models import User
from django.dispatch import receiver                 # receiver is a decorator
from .models import profile

@receiver(post_save,sender=User)                      # who sends the signal and which type of signal
def build_profile(sender,instance,created,**kwargs):   # crated holds a boolean value either user is created or not
    if created:
        profile.objects.create(user=instance)          # create an object
        
        
@receiver(post_save,sender=User)        
def save_profile(sender,instance,**kwargs):          # **kwargs is for additional keyword arguements
    instance.profile.save()
    
    