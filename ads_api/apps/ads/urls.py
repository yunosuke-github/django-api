from rest_framework.routers import SimpleRouter
from ads_api.apps.ads.views import AdViewSet

router = SimpleRouter()
router.register(r'ads', AdViewSet)

urlpatterns = router.urls
