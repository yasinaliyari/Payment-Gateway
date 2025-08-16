from django.urls import path
from purchase.views import PurchaseCreateView, PurchaseListView

urlpatterns = [
    path(
        "create/<int:package_id>/", PurchaseCreateView.as_view(), name="create-purchase"
    ),
    path("list/", PurchaseListView.as_view(), name="list-purchase"),
]
