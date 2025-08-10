from rest_framework import viewsets
from ads_api.apps.campaigns.models import AdGroup
from ads_api.apps.campaigns.serializers import AdGroupSerializer


class AdGroupViewSet(viewsets.ModelViewSet):
    queryset = AdGroup.objects.all()
    serializer_class = AdGroupSerializer
