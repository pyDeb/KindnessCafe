from django.shortcuts import render
from News.models import News
from Stats.models import StatItem
from .models import Homepage
# Create your views here.

def index(request):
    num_of_news = len(News.objects.all())
    news1 = ""
    news2 = ""
    news3 = ""
    text_body = Homepage.objects.all()[0].text_body
    if num_of_news > 0:
        news1 = News.objects.all()[num_of_news - 1]

    if num_of_news > 1:
        news2 = News.objects.all()[num_of_news - 2]

    if num_of_news > 2:
        news3 = News.objects.all()[num_of_news - 3]

    first_name = ""
    if request.session.has_key('id'):
        if User.objects.filter(id=request.session['id'])[0].is_active:
            first_name = User.objects.filter(id=request.session['id'])[0].first_name
    return render(request, 'index.html',
                  {'first_name': first_name, 'num': num_of_news, 'news1': news1, 'news2': news2, 'news3': news3,
                   'stat_items': StatItem.objects.all(), 'text_body': text_body})
