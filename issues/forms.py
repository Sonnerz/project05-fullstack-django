from django import forms
from .models import Bug


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'details', 'image', 'tag', 'published_date')
