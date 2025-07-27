from django import forms
from .models import item

class itemform(forms.ModelForm):
    class Meta:
        model = item         # --> tell django that we have to use a particular model item for this class
        fields = ['item_name','item_desc','item_price','item_image']