from rest_framework import viewsets
from ads_api.apps.accounts.models import Customer
from ads_api.apps.accounts.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
