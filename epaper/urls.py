from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_epaper, name='upload_epaper'),
    path('', views.epaper_list, name='epaper_list'),
]
