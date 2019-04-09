from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'files'

urlpatterns = [
        path('index', views.index, name='index'),
        path('authenticateuser', views.authenticate_user, name='authenticateuser'),
		path('downloadfile/<int:user_id>/<int:content_id>', views.download_file, name='downloadfile'),
        path('logoutwebcut', views.logout_webcut, name='logoutwebcut'),
        path('listuploadedfiles', views.list_uploaded_files, name='listuploadedfiles'),
        ]
