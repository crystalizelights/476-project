
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('vendor.urls')),
    path('stores/', include('stores.urls')),
    path('my_store/' , include('my_store.urls')),
    path('inbox/', include('vendor.urls')),
    #path('reviews/', include('review.urls')),
    path('admin/', admin.site.urls),

]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
