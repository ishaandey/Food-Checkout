from django import forms
from django.utils.timezone import now
class ItemForm(forms.Form):
    item_name = forms.CharField(
        label='Item Name', 
        max_length=100,            
        error_messages={'required': 'Please enter item name'},
        required=True,
        )
    comment = forms.CharField(
        label='Optional Comment', 
        max_length=500,
        required=False,
        )
    exp_date = forms.DateField(
        initial=now,
        input_formats=['%m/%d/%y']
        )


    
    
