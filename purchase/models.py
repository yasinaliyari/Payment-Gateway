from django.contrib.auth.models import User
from django.db import models, transaction
from finance.models import Payment
from package.models import Package


class Purchase(models.Model):
    PAID = 10
    NOT_PAID = -10

    STATUS_CHOICES = (
        (PAID, "Paid"),
        (NOT_PAID, "Not Paid"),
    )

    user = models.ForeignKey(
        User, related_name="purchases", on_delete=models.SET_NULL, null=True
    )
    package = models.ForeignKey(
        Package, related_name="purchases", on_delete=models.SET_NULL, null=True
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    price = models.PositiveBigIntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NOT_PAID)
    payment = models.ForeignKey(
        Payment,
        related_name="purchases",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user} >> {self.package}"

    @staticmethod
    def create_payment(package, user):
        return Payment.objects.create(amount=package.price, user=user)

    @classmethod
    def create(cls, package, user):
        if package.is_enable:
            with transaction.atomic():
                payment = cls.create_payment(package, user)
                purchase = cls.objects.create(
                    user=user, package=package, price=package.price, payment=payment
                )
            return purchase
        return None
