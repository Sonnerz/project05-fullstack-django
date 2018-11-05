from django.contrib import admin
from .models import Bug, BugComment, Feature

# Register your models here.
admin.site.register(Bug)
admin.site.register(BugComment)
admin.site.register(Feature)
