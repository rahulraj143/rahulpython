from django import forms
from .models import Todo
class Todoforms(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["name","priority","date"]
