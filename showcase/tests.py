from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    def test_homepage_shows_pricing_gallery_and_order_link(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "$30")
        self.assertContains(response, "Pastel daydream")
        self.assertContains(response, "Burgundy mood")
        self.assertContains(response, "https://www.instagram.com/eviespressons/")

    def test_static_export_contains_page_and_images(self):
        call_command("export_site", verbosity=0)
        site = Path(settings.BASE_DIR) / "site"
        html = (site / "index.html").read_text()
        self.assertIn('href="static/css/site.css"', html)
        self.assertTrue((site / "static/images/pastel-3d.jpg").is_file())
        self.assertTrue((site / "static/images/burgundy-blue.jpg").is_file())
        self.assertTrue((site / ".nojekyll").is_file())
