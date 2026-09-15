from django.test import TestCase
from django.urls import reverse


class CaletaViewsTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'La caleta')
        self.assertContains(response, 'Ceviche de reineta')

    def test_detail_page_loads(self):
        response = self.client.get(reverse('detalle', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ceviche de reineta')
