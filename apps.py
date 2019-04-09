from django.apps import AppConfig
from django.db.models.signals import post_delete
from .signals import delete_user_file, delete_user_folder

class FilesConfig(AppConfig):
	name = 'files'
	
	def ready(self):
		""" Registration for signal post_delete """

		Content = self.get_model('Content')
		post_delete.connect(delete_user_file, sender=Content, dispatch_uid='dsfsdfsdfsdfewrewrvgbcb')
		
		from django.contrib.auth.models import User
		post_delete.connect(delete_user_folder, sender=User, dispatch_uid='erwrnnsdv889fssdfs')

