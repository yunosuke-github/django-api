from rest_framework import serializers
from ads_api.apps.campaigns.models import AdGroup


class AdGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdGroup
        fields = ['id', 'campaign', 'name', 'status', 'cpc_bid']
