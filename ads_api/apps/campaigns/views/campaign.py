from rest_framework import viewsets
from ads_api.apps.campaigns.models import Campaign
from ads_api.apps.campaigns.serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
