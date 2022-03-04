from django import forms
from app1.models import students_admin

class studentforms(forms.ModelForm):
    class Meta:
        model = students_admin #students is a veriable from models.py table name
        fields = '__all__'