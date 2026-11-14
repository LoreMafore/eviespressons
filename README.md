# Evie's Press Ons

A small Django lookbook for custom press-on nails. The site uses Evie's supplied logo and nail photos. Sets start at **$30**, with add-ons quoted through [@eviespressons on Instagram](https://www.instagram.com/eviespressons/).

## Run locally

With Nix:

```sh
nix develop
python manage.py runserver
```

Or with Python 3.10+:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Visit http://127.0.0.1:8000/. To check the project and build the GitHub Pages files:

```sh
python manage.py check
python manage.py test
python manage.py export_site
```

The export command renders the Django homepage to `site/index.html` and copies local assets to `site/static/`. GitHub Pages serves this **static export**, not a live Django server. Pushes to `main` run the Pages workflow in `.github/workflows/pages.yml`. Orders and final add-on pricing are handled by Evie on Instagram; this site does not collect customer information or payments.

To update the gallery, replace images in `static/images/` and edit the set descriptions in `showcase/views.py`. The source PDFs are intentionally excluded from the public repository.
