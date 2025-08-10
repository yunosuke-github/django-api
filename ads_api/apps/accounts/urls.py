from rest_framework.routers import SimpleRouter
from ads_api.apps.accounts.views import CustomerViewSet

router = SimpleRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = router.urls
