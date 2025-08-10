from rest_framework.routers import SimpleRouter
from ads_api.apps.reports.views import ReportCampaignDailyViewSet

router = SimpleRouter()
router.register(r'campaign-daily', ReportCampaignDailyViewSet)

urlpatterns = router.urls
