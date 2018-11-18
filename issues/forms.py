from django import forms
from .models import Bug, Feature, BugComment


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'details', 'image',
                  'tag', 'published_date')


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'details', 'tag', 'published_date', 'cost_per_hour')


class AdminBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'details', 'image',
                  'tag', 'published_date', 'status')


class AdminFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'details', 'tag', 'published_date', 'status')


class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('comment',)
