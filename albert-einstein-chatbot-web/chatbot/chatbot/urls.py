from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('home.urls')),
	path('home/', include('home.urls')),
	path('chat/', include('chat.urls')),
	path("admin/", admin.site.urls),
]
