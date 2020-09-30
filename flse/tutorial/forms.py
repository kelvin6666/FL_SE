
from django import forms
from .models import FilesAdmin

class DocumentForm(forms.ModelForm):
    class Meta:
         model = FilesAdmin
         fields = ['file', 'title']