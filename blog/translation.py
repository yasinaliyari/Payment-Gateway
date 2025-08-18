from modeltranslation.translator import TranslationOptions, register
from blog.models import Post


@register(Post)
class PostTranslation(TranslationOptions):
    fields = (
        "title",
        "body",
    )
