from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        #Below controls user input. 
        fields = ['title', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateTimeInput(
                format= '%m/%d/%Y %H:%M',
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'datetime-local'
                }
            )
        }

