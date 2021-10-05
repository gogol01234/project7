from app1 import models
from django import forms
from django.db.models import fields
from app1.models import Blog

class Edit_Blog(forms.ModelForm):
    title = forms.CharField(label = "Title", widget = forms.TextInput(attrs = {"class":"form-control"}))
    dsc = forms.CharField(label = "Description", widget = forms.Textarea(attrs = {"class":"form-control"}))
    class Meta:
        model = Blog
        fields = ["title", "dsc"]
