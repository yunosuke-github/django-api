from rest_framework import serializers
from ads_api.apps.ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'ad_group', 'type', 'status', 'final_url', 'headline', 'description']
