from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'files'

urlpatterns = [
        path('index', views.index, name='index'),
        path('actionfile', views.action_file, name='actionfile'),
		path('downloadfile/<int:user_id>/<int:content_id>', views.download_file, name='downloadfile'),
        path('loginview', auth_views.LoginView.as_view())
        ]
