from django import forms
from .models import userInformation

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = userInformation
        fields = '__all__'
