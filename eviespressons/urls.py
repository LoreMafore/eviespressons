from django.urls import path

from showcase.views import home

urlpatterns = [path("", home, name="home")]
