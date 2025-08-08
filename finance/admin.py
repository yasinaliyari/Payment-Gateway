from django.contrib import admin
from finance.models import Payment, Gateway

admin.site.register(Payment)
admin.site.register(Gateway)
