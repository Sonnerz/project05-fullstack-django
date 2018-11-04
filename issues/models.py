from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Bug(models.Model):
    """
    A single Bug
    """
    title = models.CharField(max_length=100, blank=False)
    details = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    votes = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    author = models.ForeignKey(User, default=None)
    ref = models.CharField(editable=False, max_length=10)

    def __unicode__(self):
        return self.title


class BugComment(models.Model):
    """
    A single Bug Comment
    """
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, default=None, related_name="author_of_comment")
    bug = models.ForeignKey(Bug, default=None, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title


class Feature(models.Model):
    """
    A single Feature
    """
    title = models.CharField(max_length=100)
    details = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    votes = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, default=None)

    def __unicode__(self):
        return self.title
