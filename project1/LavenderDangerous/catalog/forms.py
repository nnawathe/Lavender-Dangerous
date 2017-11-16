from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class SubmitRequestForm(forms.Form):
    product_name = forms.CharField(max_length=200, help_text="Enter name of product")
    description = forms.CharField(max_length=500, help_text="Enter description of product")

    def clean_renewal_date(self):
        data = self.cleaned_data['product_name', 'description']
        
        if not data['product_name']:
            raise ValidationError(_('Product name cannot be empty'))

        if data['cost'] <= 0:
            raise ValidationError(_('Cost must be greater than 0'))
        return data