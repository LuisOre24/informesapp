from django.urls import path
from .views import RegistroView, RegistroCreate

urlpatterns = [
    path('informes', RegistroView.as_view(), name='informes'),
    path('registro', RegistroCreate.as_view(), name='registro')
]