from django.contrib.auth.models import User
from django.db import models

from stores.models import Stores
# Create your models here.
class Review(models.Model):
    stores = models.ForeignKey(Stores, related_name='reviews', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
    
class ReviewText(models.Model):
    review = models.ForeignKey(Review, related_name='texts', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_texts', on_delete=models.CASCADE)

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Viewer', 'Viewer'),
        ('Seller', 'Seller'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    userType = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='Viewer',
    )
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'