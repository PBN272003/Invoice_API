
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice

class InvoiceTests(APITestCase):
    def setUp(self):
        self.invoice_data = {
            'date': '2023-07-01',
            'invoice_no': 'INV-001',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Item 1',
                    'quantity': 2,
                    'unit_price': 10.0,
                    'price': 20.0
                },
                {
                    'description': 'Item 2',
                    'quantity': 3,
                    'unit_price': 15.0,
                    'price': 45.0
                }
            ]
        }

    def test_create_invoice(self):
        url = reverse('invoices-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_get_invoice_list(self):
        Invoice.objects.create(date='2023-07-01', invoice_no='INV-001', customer_name='John Doe')
        url = reverse('invoices-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_invoice_detail(self):
        invoice = Invoice.objects.create(date='2023-07-01', invoice_no='INV-001', customer_name='John Doe')
        url = reverse('invoices-detail', args=[invoice.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'John Doe')

