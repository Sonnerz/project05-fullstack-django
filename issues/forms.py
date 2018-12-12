from django import forms
from .models import Bug, Feature, BugComment


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('title', 'details', 'image',
                  'tag', 'published_date')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add bug title'}),
            'tag': forms.TextInput(attrs={'placeholder': 'Add keywords for example; bug, feature, error...'}),
            'details': forms.Textarea(attrs={'placeholder': 'Add bug details...'})
        }


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'details', 'tag', 'published_date', 'cost_per_hour')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add feature title'}),
            'tag': forms.TextInput(attrs={'placeholder': 'Add keywords for example; bug, feature, error...'}),
            'details': forms.Textarea(attrs={'placeholder': 'Add feature details...'})
        }


class AdminBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'details', 'image',
                  'tag', 'published_date', 'status')


class AdminFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'details', 'tag',
                  'published_date', 'status', 'dev_hours_req', 'is_new')
        widgets = {
            'dev_hours_req': forms.TextInput(attrs={'placeholder': 'Hours required to develop the feature'}),
        }
        labels = {
            "is_new": ("Is this a new feature?"),
            "dev_hours_req": ("Development hours required")
        }


class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Add a comment about this bug'})
        }
