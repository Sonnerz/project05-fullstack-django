# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django import template

# Third-party app imports

# Realative imports of the 'app-name' package


register = template.Library()


@register.filter('has_group')
def has_group(user, group_name):
    """
    Check if user is in a group
    """
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False
