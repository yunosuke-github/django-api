from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/accounts/', include('ads_api.apps.accounts.urls')),
    path('api/campaigns/', include('ads_api.apps.campaigns.urls')),
    path('api/ads/', include('ads_api.apps.ads.urls')),
    path('api/reports/', include('ads_api.apps.reports.urls')),
]
