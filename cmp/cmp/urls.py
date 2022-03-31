from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cmp_admin/', include('cmp_admin.urls')),
    path('admin/', admin.site.urls)
]
