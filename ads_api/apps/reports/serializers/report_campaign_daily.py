from rest_framework import serializers
from ads_api.apps.reports.models import ReportCampaignDaily


class ReportCampaignDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCampaignDaily
        fields = ['customer', 'campaign', 'date', 'impressions', 'clicks', 'cost', 'conversions']
