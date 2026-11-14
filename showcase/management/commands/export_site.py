"""Render the Django homepage into a self-contained GitHub Pages artifact."""

import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client


class Command(BaseCommand):
    help = "Export the Django homepage and local assets to site/ for static hosting"

    def handle(self, *args, **options):
        destination = Path(settings.BASE_DIR) / "site"
        destination.mkdir(exist_ok=True)
        response = Client().get("/")
        if response.status_code != 200:
            raise RuntimeError(f"Homepage returned {response.status_code}")
        # Django emits root-relative static URLs for local development. Pages
        # project sites live under /<repository>/, so export relative URLs.
        html = response.content.decode("utf-8").replace('"/static/', '"static/')
        (destination / "index.html").write_text(html, encoding="utf-8")
        shutil.copytree(settings.BASE_DIR / "static", destination / "static", dirs_exist_ok=True)
        (destination / ".nojekyll").touch()
        self.stdout.write(self.style.SUCCESS(f"Exported website to {destination}"))
