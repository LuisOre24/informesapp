from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistroView, RegistroCreate

urlpatterns = [
    path('informes', login_required(RegistroView.as_view()), name='informes'),
    path('registro', login_required(RegistroCreate.as_view()), name='registro')
]