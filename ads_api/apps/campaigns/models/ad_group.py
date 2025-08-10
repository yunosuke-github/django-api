import uuid
from django.db import models
from .campaign import Campaign


class AdGroup(models.Model):
    STATUS_CHOICES = [
        ('ENABLED', 'Enabled'),
        ('PAUSED', 'Paused'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='ad_groups')
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ENABLED')
    cpc_bid = models.DecimalField(max_digits=18, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name
