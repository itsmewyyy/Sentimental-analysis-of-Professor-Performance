
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('userLogin.urls')),
    path('api/', include('SET.urls')),
    path('api/', include('reportsAnalysis.urls')),
    ]
