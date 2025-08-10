from rest_framework import serializers
from ads_api.apps.accounts.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'time_zone', 'currency', 'manager']
