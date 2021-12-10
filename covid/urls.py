from django.urls import path
from . import views

urlpatterns = [
    path('', views.data, name= 'data'),
    # path('dashboard', views.data, name= 'dashboard'),
    path('nasio', views.nasio, name= 'nasio'),
    # path('map', views.map, name= 'map'),
    path('chart', views.chart, name= 'chart'),
]