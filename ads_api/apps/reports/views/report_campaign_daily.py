from rest_framework import viewsets
from ads_api.apps.reports.models import ReportCampaignDaily
from ads_api.apps.reports.serializers import ReportCampaignDailySerializer


class ReportCampaignDailyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReportCampaignDaily.objects.all()
    serializer_class = ReportCampaignDailySerializer
