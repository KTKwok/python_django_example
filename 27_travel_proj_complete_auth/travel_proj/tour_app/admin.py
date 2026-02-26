from django.contrib import admin
from django.utils.html import format_html
from .models import Destination, TourCategory


# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['image_thumb', 'name', 'is_featured']

    @admin.display(description='Image')
    def image_thumb(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html(
                "<img src='{}' width='64' height='32'/>",
                obj.image.url
            )
        return "-"

@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name']