from .models import Bug, Feature
import django_filters


class BugsFilter(django_filters.FilterSet):
    '''
    Filter the bugs by status field
    '''
    class Meta:
        model = Bug
        fields = ['status']


class FeaturesFilter(django_filters.FilterSet):
    '''
    Filter the features by status field
    '''
    class Meta:
        model = Feature
        fields = ['status']
