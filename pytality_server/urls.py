from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('pytality_server.api.urls')),
    path('admin/', admin.site.urls),
]
