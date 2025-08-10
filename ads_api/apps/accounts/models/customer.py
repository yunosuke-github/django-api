import uuid
from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    time_zone = models.CharField(max_length=64, default='UTC')
    currency = models.CharField(max_length=3, default='USD')
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_accounts')

    def __str__(self):
        return self.name
