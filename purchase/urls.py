from django.urls import path

from purchase.views import PurchaseCreateView

urlpatterns = [
    path(
        "create/<int:package_id>/", PurchaseCreateView.as_view(), name="create-purchase"
    )
]
