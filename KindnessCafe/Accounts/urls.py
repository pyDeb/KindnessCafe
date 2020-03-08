from django.urls import path
from .views import HomePageView, SignupPageView, Index


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index/', Index.as_view(), name='index'),
    path('signup/', SignupPageView.as_view(), name='signup'), 
]