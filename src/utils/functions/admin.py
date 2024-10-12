from django.utils import html


def get_image_with_tag(instance, image_field=None):
    image = getattr(instance, image_field)
    return html.format_html(
        '<img src="{}" style="max-width:150px; max-height:150px"/>'.format(image.url)
    )
