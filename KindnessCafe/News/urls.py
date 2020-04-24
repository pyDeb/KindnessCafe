from django.urls import path
from .views import single_news_page
from .models import News

urlpatterns = [
    path('news/<int:id>', single_news_page, name='single_news_page'),
    

]