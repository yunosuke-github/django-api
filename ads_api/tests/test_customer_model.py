from django.test import TestCase
from ads_api.apps.accounts.models import Customer


class CustomerModelTest(TestCase):
    def test_defaults_and_str(self):
        customer = Customer.objects.create(name="Test Customer")
        self.assertEqual(customer.time_zone, "UTC")
        self.assertEqual(customer.currency, "USD")
        self.assertEqual(str(customer), "Test Customer")
