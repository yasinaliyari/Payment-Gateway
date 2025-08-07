from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=48)
    price = models.PositiveBigIntegerField()
    description = models.TextField(blank=True)
    days = models.PositiveBigIntegerField()
    is_enable = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
