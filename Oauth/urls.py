from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_anme = 'Oauth'
urlpatterns = [
    path('', views.stuff_login, name='stuff_login'),
    path('dashboard/', views.stuff_login, name = 'dashboard'),
    path('register/', views.stuff_register, name = 'stuff_register'),
    path('profile/', views.stuff_profile, name = 'stuff_profile'),
    path('teachers/', views.all_stuff, name = 'all_stuff'),
    path('teacher/<int:id>', views.stuff_detail, name = 'stuff_detail'),
    path('teacher/edit/<int:id>', views.edit_stuff, name = 'edit_stuff'),
    path('profile/add', views.stuff_create_profile, name = 'create_profile'),
    path('deletestuff', views.delete_stuff_profile, name = 'delete_stuff'),
    path('logout/', views.user_loguot, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)