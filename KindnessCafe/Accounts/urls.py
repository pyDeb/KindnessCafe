from django.urls import path
from .views import HomePageView, SignupPageView, Index, CustomLoginView, ContactUsPageView, OurMissionPageView
from News.views import NewsPageView
from class_based_auth_views.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignupPageView.as_view(), name='signup'), 
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('news/', NewsPageView.as_view(), name='news'), 
    path('contact/', ContactUsPageView.as_view(), name='contact'), 
    path('ourmission/', OurMissionPageView.as_view(), name='ourmission'), 
]