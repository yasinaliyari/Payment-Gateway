from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    body = models.TextField(verbose_name=_("body"))
    create_time = models.DateTimeField(verbose_name=_("create time"), auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=_("modified time"), auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
