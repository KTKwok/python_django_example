from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='tour_app/destination_img/', blank=True, null=True)
    is_featured = models.BooleanField(verbose_name="Featured", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
        ordering = ['name']

class TourCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="The icon from Bootstrap, e.g. bi bi-7-circle")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tour Category"
        verbose_name_plural = "Tour Categories"