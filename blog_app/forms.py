from django import forms

from .models import Headline, Text

class HeadlineForm(forms.ModelForm):
    class Meta:
        model = Headline
        fields = ['headline_text']
        labels = {'headline_text': ''}

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}