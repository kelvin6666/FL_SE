from django import forms
from .models import comment,question
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']

class SolutionForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['r_token']


			
