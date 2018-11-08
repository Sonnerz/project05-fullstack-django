from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Donor(models.Model):
    user = models.ForeignKey(User)
    is_donor = models.BooleanField(default=False)
    
User.profile = property(lambda u: Donor.objects.get_or_create(user=u)[0])
