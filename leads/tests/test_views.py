from django.test import TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
    
    