from .models import Bug, Feature
import django_filters


class BugsFilter(django_filters.FilterSet):
    class Meta:
        model = Bug
        fields = ['status']


class FeaturesFilter(django_filters.FilterSet):
    class Meta:
        model = Feature
        fields = ['status']
