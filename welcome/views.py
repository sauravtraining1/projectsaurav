from django.shortcuts import render
from .models import Post

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'welcome/Boot.html', context)                                                                                                                   

def about(request):
	return render(request, 'welcome/about.html', {'title':'About'})