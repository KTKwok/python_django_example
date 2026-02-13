from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(verbose_name="Gender", max_length=100, default="Male")
    created_at = models.DateTimeField(verbose_name="Create At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Update At", auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(verbose_name="Title",max_length=100)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Create At", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Update At", auto_now=True)

    def __str__(self):
        return f"{self.title}"