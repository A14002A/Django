from django import forms
from .models import *



class MovieForm(forms.ModelForm):
    class Meta:
        Movie = models
        fields = ('name', 'director', 'text', 'description', 'release_date', 'image')

class ReviewForm(forms.ModelForm):
    class Meta:
        Review = models
        fields = ("comment", "rating")
      