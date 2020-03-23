from django.urls import path
from .views import NewsSinglePageView
from .models import News

urlpatterns = [
    path('news/<int:pk>', NewsSinglePageView.as_view(), name='news_single_page'),

]