from django.urls import path, include
#from django.views.generic import TemplateView
from .views import ClearenceCreatinina

app_name = 'ajuste_dose'

urlpatterns = [
    path('', ClearenceCreatinina.as_view(), name='ajustedose'),
]