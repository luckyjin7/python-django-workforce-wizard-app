from django import forms
from .models import UserList

class ListForm(forms.ModelForm):
    class Meta:
        model = UserList
        fields="__all__"