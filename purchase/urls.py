from django.urls import path
from purchase.views import PurchaseCreateView, purchases_list

urlpatterns = [
    path(
        "create/<int:package_id>/", PurchaseCreateView.as_view(), name="create-purchase"
    ),
    path("list/", purchases_list, name="list-purchase"),
    path("list/<str:username>/", purchases_list, name="list-purchase"),
]
