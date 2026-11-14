from django.shortcuts import render


def home(request):
    return render(request, "showcase/home.html", {
        "instagram": "https://www.instagram.com/eviespressons/",
        "sets": [
            {
                "name": "Pastel daydream",
                "detail": "Pastel ombré · sculpted 3D details · a little sparkle",
                "image": "images/pastel-3d.jpg",
                "alt": "Long pastel pink, mint, and lavender nails with glitter and sculpted black cat details",
                "number": "01",
            },
            {
                "name": "Burgundy mood",
                "detail": "Deep burgundy · baby blue · hand-painted accents",
                "image": "images/burgundy-blue.jpg",
                "alt": "Long pointed burgundy and baby blue nails with hand-painted details",
                "number": "02",
            },
        ],
    })
