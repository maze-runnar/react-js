from django.shortcuts import render, get_object_or_404,redirect
from .models import Guides
from django.views.generic.list import ListView
from .forms import RegisterForm
import operator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']



from django.db.models import Q

# Create your views here.
@login_required
def main(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return render(request,'login.html',{})
	else:
		queryset  = Guides.objects.all()
		context = {
				"object_list" : queryset,
		}
	return render(request, 'home.html',context)
@login_required
def search(request):
	template = 'search.html'
	query = request.GET.get('q')
	if query:
		results = Guides.objects.filter(Q(area__icontains= query) | Q(name__icontains = query))
	else:
		results = Guides.objects.all()
	context = {
			"items":results
	} 
	return render(request, 'search.html', context)
@login_required
def logout_user(request):
    logout(request)
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect("http://127.0.0.1:8000/accounts/login")

@login_required
def register(request):
	# if not request.user.is_authenticated:
	# 	return render(request, 'login.html',{})
	# else:
	form = RegisterForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		album = form.save(commit=False)
		album.album_logo = request.FILES['album_logo']
		file_type = album.album_logo.url.split('.')[-1]
		file_type = file_type.lower()
		if file_type not in IMAGE_FILE_TYPES:
			context = {
			    'album': album,
			    'form': form,
			    'error_message': 'Image file must be PNG, JPG, or JPEG',
			}
			return render(request, 'create.html', context)
		album.save()
		form = RegisterForm()

	context = {
			'form' : form
	}
	return render(request, 'create.html', context)

@login_required
def detail(request,id):
	if not request.user.is_authenticated:
		return render(request, 'login.html',{})
	else:
		obj = Guides.objects.get(id=id)
		context = {'object'  : obj}
	return render(request, "detail.html",context)

@login_required
def guide_profile(request, id):
	if not request.user.is_authenticated:
		return render(request, 'login.html',{})
	else:
		
		return render(request, "profile.html")

