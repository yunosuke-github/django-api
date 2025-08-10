from rest_framework.routers import SimpleRouter
from ads_api.apps.campaigns.views import CampaignViewSet, AdGroupViewSet

router = SimpleRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'ad-groups', AdGroupViewSet)

urlpatterns = router.urls
