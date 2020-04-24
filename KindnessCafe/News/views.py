from django.shortcuts import render
from .models import News
from Accounts.models import User

# Create your views here.
def news_view(request):
	first_name = ""
	if request.session.has_key('id'):
		first_name = User.objects.filter(id=request.session['id'])[0].first_name
	return render(request, 'news.html', {'news' : News.objects.all(), 'first_name' : first_name})




def single_news_page(request, id):	
	item = News.objects.filter(id=id)[0]
	first_name = ""
	if request.session.has_key('id'):
		first_name = User.objects.filter(id=request.session['id'])[0].first_name
	return render(request, 'newsSinglePage.html', {'item' : item, 'first_name' : first_name})