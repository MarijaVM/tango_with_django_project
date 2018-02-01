from django import models
from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=128, help_text='Please enter the category name.')
    views=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes=forms.IntegerField(widget=forms.HiddenInput(), initial=0)