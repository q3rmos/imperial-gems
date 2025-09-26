from django import template
from django.templatetags.static import static
import os
from django.conf import settings

register = template.Library()


@register.simple_tag
def image_or_placeholder(field, placeholder="jewelry/images/default-product.webp"):
    """
    Возвращает URL картинки или заглушку, если файла нет/битый путь.
    """
    try:
        if field and getattr(field, "url", None):
            # путь на диске
            filepath = os.path.join(settings.MEDIA_ROOT, str(field))
            if os.path.exists(filepath):
                return field.url
    except Exception:
        pass
    return static(placeholder)
