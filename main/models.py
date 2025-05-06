from django.db import models
#
from django.db import models


class Basic(models.Model):
    title = models.CharField(max_length=100, blank=True)
