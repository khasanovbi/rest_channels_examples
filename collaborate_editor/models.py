from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
