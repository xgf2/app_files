import os
#from webcut import settings as webcut_settings
from django.conf import settings as webcut_settings
from files import settings as files_settings

def delete_user_file(sender, instance, **kwargs):
	#instance.file.delete()
	path_file = webcut_settings.MEDIA_ROOT + instance.file.name
	if instance.file:
		if os.path.isfile(path_file):
			os.remove(path_file)	

def delete_user_folder(sender, instance, **kwarg):
	path_folder = webcut_settings.MEDIA_ROOT + files_settings.FILES_ROOT + str(instance.id)
	if os.path.isdir(path_folder):
		os.rmdir(path_folder)

