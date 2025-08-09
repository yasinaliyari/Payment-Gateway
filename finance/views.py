from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from finance.forms import ChargeWalletForm
from finance.models import Payment, Gateway
from finance.utils.zarinpal import zpal_request_handler, zpal_payment_checker


class ChargeWalletView(View):
    template_name = "charge_wallet.html"
    form_class = ChargeWalletForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            payment_link, authority = zpal_request_handler(
                settings.ZARINPAL["merchant_id"],
                form.cleaned_data["amount"],
                "Wallet charge",
                "yasinaliyari30@gmail.com",
                None,
                settings.ZARINPAL["gateway_callback_url"],
            )
            if payment_link is not None:
                return redirect(payment_link)

        return render(request, self.template_name, {"form": form})


class VerifyView(View):
    template_name = "callback.html"

    def get(self, request, *args, **kwargs):
        status = request.GET.get("Status")
        authority = request.GET.get("Authority")
        try:
            payment = Payment.objects.get(authority=authority)
        except Payment.DoesNotExist:
            raise Http404

        if status != "OK":
            return render(
                request,
                self.template_name,
                {"is_paid": False},
            )

        data = dict(
            merchant_id=payment.gateway.auth_data,
            amount=payment.amount,
            authority=payment.authority,
        )
        payment.verify(data)
        return render(request, self.template_name, {"payment": payment})


class PaymentView(View):
    def get(self, request, invoice_number, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404

        gateways = Gateway.objects.filter(is_enable=True)

        return render(
            request,
            "finance/payment_detail.html",
            {"payment": payment, "gateways": gateways},
        )


class PaymentGatewayView(View):
    def get(self, request, invoice_number, gateway_code, *args, **kwargs):
        try:
            payment = Payment.objects.get(invoice_number=invoice_number)
        except Payment.DoesNotExist:
            raise Http404

        try:
            gateway = Gateway.objects.get(gateway_code=gateway_code)
        except Gateway.DoesNotExist:
            raise Http404

        payment.gateway = gateway
        payment.save()
        payment_link = payment.bank_page
        if payment_link:
            return redirect(payment_link)

        gateways = Gateway.objects.filter(is_enable=True)
        return render(
            request,
            "finance/payment_detail.html",
            {"payment": payment, "gateways": gateways},
        )
