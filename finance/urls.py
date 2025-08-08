from django.urls import path

from finance.views import ChargeWalletView, VerifyView, PaymentView, PaymentGatewayView

urlpatterns = [
    path("charge/", ChargeWalletView.as_view(), name="charge-wallet"),
    path("verify/", VerifyView.as_view(), name="verify-view"),
    path("pay/<str:invoice_number>/", PaymentView.as_view(), name="payment-link"),
    path(
        "pay/<str:invoice_number>/<str:gateway_code>/",
        PaymentGatewayView.as_view(),
        name="payment-gateway",
    ),
]
