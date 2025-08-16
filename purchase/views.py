from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from package.models import Package
from purchase.models import Purchase


class PurchaseCreateView(LoginRequiredMixin, View):
    def get(self, request, package_id, *args, **kwargs):
        try:
            package = Package.objects.get(id=package_id)
        except Package.DoesNotExist:
            raise Http404

        purchase = Purchase.create(package, request.user)
        return render(request, "purchase/create.html", {"purchase": purchase})


@cache_page(200)
def purchases_list(request, username):
    purchases = Purchase.objects.all()
    if username is not None:
        purchases = purchases.filter(user__username=username)
    print("View touched")
    return render(request, "purchase/list.html", {"purchases": purchases})


@method_decorator([cache_page(200), vary_on_cookie], name="dispatch")
class PurchaseListView(View):
    def get(self, request, username=None, *args, **kwargs):
        purchases = Purchase.objects.all()
        if username is not None:
            purchases = purchases.filter(user__username=username)
        print("View touched")
        return render(request, "purchase/list.html", {"purchases": purchases})
