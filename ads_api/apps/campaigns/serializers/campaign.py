from rest_framework import serializers
from ads_api.apps.campaigns.models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'customer', 'name', 'status', 'start_date', 'end_date', 'daily_budget', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
