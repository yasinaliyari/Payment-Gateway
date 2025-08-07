from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("pricing/", TemplateView.as_view(template_name="package/pricing.html"))
]
