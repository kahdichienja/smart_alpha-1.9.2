from django.urls import path
from . import views

app_anme = 'Library'
urlpatterns = [
    path('', views.all_asset, name = 'all_asset'),
    path('add/', views.add_asset, name = 'add_asset'),
]
