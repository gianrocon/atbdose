from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'ajuste_dose'

urlpatterns = [
    path('', TemplateView.as_view(template_name='ajuste_dose/ajuste_dose.html')),
]