from django import forms
from gallery.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'name', 'tag']
