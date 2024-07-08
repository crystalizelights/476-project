from django.contrib import admin

from .models import Review, ReviewText

admin.site.register(Review)
admin.site.register(ReviewText)