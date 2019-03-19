from django.db import models
import os
from datetime import datetime, timedelta

# Models
	
class User(models.Model):
	identifier = models.CharField(max_length = 100, unique = False)
	code = models.CharField(max_length = 100, unique = False)
	date_time = models.DateTimeField(auto_now = True)

	def __str__(self):
		return str(self.identifier)

def user_path_file(instance_content, empty_parameter):
	return 'files/{0}/{1}'.format(instance_content.user.id, instance_content.file.name)

class Content(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	file = models.FileField(upload_to = user_path_file, max_length = 100) 
	date_time = models.DateTimeField(auto_now = True)
	date_time_delete = models.DateTimeField(default = datetime.now() + timedelta(days = 5))

	def __str__(self):
		return str(self.user)

# Functions

def save_user_file(request):
	try:
		user = User.objects.get(identifier=request.POST.get('identifier'), code = request.POST.get('code'))
	except User.DoesNotExist:
		user = User(identifier = request.POST.get('identifier'), code = request.POST.get('code'))
		user.save()
	finally:
		user_file = Content(user = user, file = request.FILES.get('filename'), date_time_delete = datetime.now() + timedelta(days = 180))
		user_file.save()

def user_contents(request):
	try:
		user = User.objects.get(identifier=request.POST.get('identifier'), code = request.POST.get('code'))
		contents = user.content_set.all()
		return contents

	except User.DoesNotExist:
		return 'Files_not_exist'
		#user = User(identifier = request.POST.get('identifier'), code = request.POST.get('code'))
		#user.save()

def user_content(user_id, content_id):
	try:
		user = User.objects.get(id = user_id)
		content = user.content_set.get(id = content_id)
		return content

	except User.DoesNotExist:
		pass

