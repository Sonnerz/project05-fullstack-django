from .models import Bug
import django_filters


class BugsFilter(django_filters.FilterSet):
    class Meta:
        model = Bug
        fields = ['status']
