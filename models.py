from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from files import settings as files_settings

# Models
	
def user_path_file(instance_content, empty_parameter):
	return '{0}/{1}/{2}'.format(files_settings.FILES_ROOT, instance_content.user.id, instance_content.file.name)

class Content(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	file = models.FileField(upload_to = user_path_file, max_length = 100) 
	date_time = models.DateTimeField(auto_now = True)
	date_time_delete = models.DateTimeField(default = datetime.now() + timedelta(days = 5))

	def __str__(self):
		return str(self.file.name)

# Functions

def save_user_file(request):
	try:
		user = User.objects.get(username = request.user)
	except User.DoesNotExist:
		user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password'))
		user.save()
	finally:
		user_file = Content(user = user, file = request.FILES.get('filename'), date_time_delete = datetime.now() + timedelta(days = 180))
		user_file.save()

def user_contents(request):
	try:
		user = User.objects.get(username = request.user)
		contents = user.content_set.all()
		return contents

	except User.DoesNotExist:
		return  None

def user_content(user_id, content_id):
	try:
		user = User.objects.get(id = user_id)
		content = user.content_set.get(id = content_id)
		return content

	except User.DoesNotExist:
		return None

def create_user(request):
	user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password'))
	user.save()
	return user

