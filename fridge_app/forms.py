from django import forms
from django.utils.timezone import now
from .widgets import BootstrapDateTimePickerInput


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
    exp_date = forms.CharField(
        # initial=now,
        required=False,
        max_length=500,
        )
    # exp_date = forms.DateTimeField(
    #     input_formats=['%m/%d/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'})
    # )
            