from django.urls import path
from .views import home, agenda, registro
from django.views.generic import RedirectView
urlpatterns = [
    path('', home, name='home'),
    path('agenda/', agenda, name="agenda"),
    path('registro/', registro, name="registro" )
]