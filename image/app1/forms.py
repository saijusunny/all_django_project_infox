from django import forms
from app1.models import images

class imageform(forms.ModelForm):
    class Meta:
        model= images
        fields = '__all__'