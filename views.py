from django.shortcuts import render

from django.http import HttpResponse
from files.forms import IdentifierData
from files.models import save_user_file, user_content, user_contents

import magic
import os
from webcut import settings

# Create your views here.

def index(request):
	return send_identifer_form(request)

def upload_file_successful(request):
	return render(request, 'files/upload_file_successful.html')

def upload_file_unsuccessful(request):
	return render(request, 'files/upload_file_unsuccessful.html') 

def list_download_files(request):
	contents = user_contents(request)
	# Override content.file.name
	if contents != 'Files_not_exist':
		for content in contents:
			content.file.name = os.path.split(content.file.name)[1]
		return render(request, 'files/list_download_files.html', {'contents': contents})
	else:
		return render(request, 'files/download_files_not_exist.html')	

def download_file(request, user_id, content_id):
	content = user_content(user_id, content_id)
	path_to_file = settings.MEDIA_ROOT + content.file.url
	content.file.open()
	response = HttpResponse(content.file.read(), content_type = magic.from_file(path_to_file, mime = True))
	response['Content-Disposition'] = 'attachment; filename="{filename}"'.format(filename = os.path.split(content.file.url)[1])
	response['Content-Length'] = content.file.size
	return response

def send_identifer_form(request):
	return render(request, 'files/index.html', {'form': IdentifierData})

def action_file(request):
	if request.method == 'POST':
		form = IdentifierData(request.POST)
		if form.is_valid():
			if request.POST.get('upload') != None and len(request.FILES) > 0: 
				save_user_file(request)
				return upload_file_successful(request)
			elif request.POST.get('download') != None:
				return list_download_files(request) 
			else:
				return render(request, 'files/empty_files.html')
		else:
			return HttpResponse(upload_file_unsuccessful(request))
	else:
		return send_identifer_form(request)


