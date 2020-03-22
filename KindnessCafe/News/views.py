from django.shortcuts import render
from django.views import generic
from .models import News

# Create your views here.
class NewsPageView(generic.ListView):
	model = News
	context_object_name = 'news'
	template_name = 'news.html'