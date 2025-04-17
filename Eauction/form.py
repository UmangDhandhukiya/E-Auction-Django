from django import forms
from .models import image
from django.conf import settings
from django.conf.urls.static import static

class ImageForm(forms.ModelForm):
    class meta:
        model=image
        field=("caption","image")