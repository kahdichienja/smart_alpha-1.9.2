from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_anme = 'Department'
urlpatterns = [
    path('departments/', views.all_department, name = 'all_department'),
    path('department/add/', views.create_department, name = 'create_department'),
    path('department/edit/<int:id>/', views.edit_department, name = "edit_department"),
    path('delete_dept/', views.delete_department, name = 'delete_department'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)