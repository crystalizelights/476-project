from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        
class Stores(models.Model):
    category = models.ForeignKey(Category, related_name='stores', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address  = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image= models.ImageField(upload_to='item_images', blank=True, null=True)
    image1 = models.ImageField(upload_to='item_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="stores", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
