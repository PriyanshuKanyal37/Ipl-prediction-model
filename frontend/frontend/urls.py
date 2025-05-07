from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls')),  # Point root to dashboard app
    path('admin/', admin.site.urls),
]
