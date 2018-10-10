from django.db import models


class Version(models.Model):
    version = models.CharField(max_length=10, null=True, blank=True)
    summary = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
