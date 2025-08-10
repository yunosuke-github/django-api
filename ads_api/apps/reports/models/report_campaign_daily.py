from django.db import models
from ads_api.apps.accounts.models import Customer
from ads_api.apps.campaigns.models import Campaign


class ReportCampaignDaily(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    date = models.DateField()
    impressions = models.BigIntegerField(default=0)
    clicks = models.BigIntegerField(default=0)
    cost = models.DecimalField(max_digits=18, decimal_places=6, default=0)
    conversions = models.BigIntegerField(default=0)

    class Meta:
        unique_together = ('customer', 'campaign', 'date')

