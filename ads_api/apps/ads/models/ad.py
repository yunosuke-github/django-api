import uuid
from django.db import models
from ads_api.apps.campaigns.models import AdGroup


class Ad(models.Model):
    STATUS_CHOICES = [
        ('ENABLED', 'Enabled'),
        ('PAUSED', 'Paused'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ad_group = models.ForeignKey(AdGroup, on_delete=models.CASCADE, related_name='ads')
    type = models.CharField(max_length=20, default='text')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ENABLED')
    final_url = models.URLField(max_length=2048)
    headline = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.headline
