from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from files.forms import IdentifierData
from files.models import save_user_file, user_content, user_contents, find_or_create_user
from django.conf import settings

import magic
import os

# Create your views here.

def index(request):
	return send_identifer_form(request)

def logout_webcut(request):
	logout(request)
	return redirect('files:index')

def upload_file_successful(request):
	return render(request, 'files/upload_file_successful.html')

def form_data_not_valid(request): #, errors):
	return render(request, 'files/form_data_not_valid.html') #, {'errors': errors}) 

def identifier_not_register(request):
	return render(request, 'files/identifier_not_register.html')

def list_uploaded_files(request):
	contents = user_contents(request)
	if contents: 
		# Override content.file.name
		for content in contents:
			content.file.name = os.path.split(content.file.name)[1]
		return render(request, 'files/list_uploaded_files.html', {'contents': contents})
	else:
		return render(request, 'files/download_files_not_exist.html')	

def download_file(request, user_id, content_id):
	content = user_content(user_id, content_id)
	if content and request.user.id == user_id and request.user.is_authenticated:
		path_to_file = settings.MEDIA_ROOT + content.file.url
		content.file.open()
		response = HttpResponse(content.file.read(), content_type = magic.from_file(path_to_file, mime = True))
		response['Content-Disposition'] = 'attachment; filename="{filename}"'.format(filename = os.path.split(content.file.url)[1])
		response['Content-Length'] = content.file.size
		return response
	else:
		return redirect('files:index')

def send_identifer_form(request):
	return render(request, 'files/index.html', {'form': IdentifierData, 'request': request})

def action_file(request):
	if request.method == 'POST':
		if request.POST.get('upload') != None and len(request.FILES) > 0: 
			save_user_file(request, find_or_create_user(request))
			return upload_file_successful(request)
		elif request.POST.get('download') != None:
			return list_uploaded_files(request) 
		else:
			return render(request, 'files/empty_files.html')
	else:
		return send_identifer_form(request)

def authenticate_user(request):
	if not request.user.is_authenticated:
		user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))
		if user is not None:
			login(request, user)
			return action_file(request)
		else:
			form = IdentifierData(request.POST)
			if form.is_valid():
				if request.POST.get('newidentifier') != None:
					user = find_or_create_user(request)
					login(request, user)
					return action_file(request)
				else:
					return identifier_not_register(request)
			else:
				print(form.errors)
				return form_data_not_valid(request) #, form.errors)
	else:
		return action_file(request)

