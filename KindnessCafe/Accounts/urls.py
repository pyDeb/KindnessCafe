from django.urls import path
from .views import HomePageView, SignupPageView, Index, CustomLoginView
from class_based_auth_views.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignupPageView.as_view(), name='signup'), 
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('contact/', LogoutView.as_view(), name='contact'), 
]