from rest_framework import viewsets
from ads_api.apps.ads.models import Ad
from ads_api.apps.ads.serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
