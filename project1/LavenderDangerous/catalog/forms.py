from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class SubmitRequestForm(forms.Form):
    product_name = forms.CharField(max_length=200, help_text="</br>")
    description = forms.CharField(max_length=200,widget=forms.Textarea, help_text="")

    def clean_request(self):
        data = self.cleaned_data['product_name', 'description']
        if not data['product_name']:
            raise ValidationError(_('Product name cannot be empty'))
            
        if not data['description']:
            raise ValidationError(_('Description cannot be empty'))
            
        return data