from django import forms
from .models import *


#contact module(user details)

class details_form(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100)
    emailid = forms.EmailField( required=True, max_length=250)
    phone = forms. CharField(max_length=11)
    message = forms.CharField(widget=forms.Textarea())

    def clean(self):
        cleaned_data = super(details_form, self).clean()
        name = cleaned_data.get('name')
        emailid = cleaned_data.get('emailid')
        phone = cleaned_data.get('phone')
        message = cleaned_data.get('message')
        if not name and not emailid and not phone and not message:
            raise forms.ValidationError('You have to fill all the fields')





    class Meta():
        model = user
        fields = ['name', 'emailid', 'phone', 'message']