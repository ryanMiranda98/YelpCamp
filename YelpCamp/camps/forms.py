from django import forms
from .models import Camp

class CreateCampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = '__all__'