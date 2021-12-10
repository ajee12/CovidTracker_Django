from django.contrib import admin
from django.urls import path
from django.urls import path, include
from covid import views

urlpatterns = [
    path('', include('covid.urls')),
    path('admin/', admin.site.urls),
    
 ]
