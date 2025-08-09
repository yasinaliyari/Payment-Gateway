from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from finance.models import Payment
from purchase.models import Purchase


@receiver(post_save, sender=Payment)
def callback(sender, instance, created, **kwargs):
    if instance.is_paid and not instance._b_is_paid:
        print("Purchase signal fired!!!")
        if instance.purchases.exists():
            purchase = instance.purchases.first()
            purchase.status = Purchase.PAID
            purchase.save()


@receiver(post_init, sender=Payment)
def store_is_paid_status(sender, instance, **kwargs):
    print("post_init signal called!!!")
    instance._b_is_paid = instance.is_paid
