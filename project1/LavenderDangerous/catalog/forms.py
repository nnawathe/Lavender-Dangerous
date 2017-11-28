from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
    
class SubmitRequestForm(forms.Form):
    product_name = forms.CharField(max_length=200, help_text="</br>")
    description = forms.CharField(max_length=200,widget=forms.Textarea, help_text="")

    def clean(self):
        data = super(SubmitRequestForm,self).clean()
        if not data['product_name']:
            raise ValidationError(_('Product name cannot be empty'))
            
        if not data['description']:
            raise ValidationError(_('Description cannot be empty'))
            
        return data
        
class SubmitReviewForm(forms.Form):
    rating = forms.IntegerField()
    review_text =  forms.CharField(max_length=1000,widget=forms.Textarea, help_text="")

    def clean(self):
        data = super(SubmitReviewForm,self).clean()
        if not data['rating']:
            raise ValidationError(_('Rating cannot be empty'))
        
        if int(data['rating'])<0 or int(data['rating'])>5:
            raise ValidationError(_('Rating must be a number from 0 to 5'))
        
        if not data['review_text']:
            raise ValidationError(_('Review cannot be empty'))
            
        return data