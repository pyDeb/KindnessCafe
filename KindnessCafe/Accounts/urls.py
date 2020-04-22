from django.urls import path
# from .views import HomePageView, SignupPageView, Index, CustomLoginView, ContactUsPageView, OurMissionPageView 
from .views import index, contact_us, our_mission, login, signup
from News.views import NewsPageView

urlpatterns = [
    # path('', Index.as_view(), name='index'),
    # path('signup/', SignupPageView.as_view(), name='signup'), 
    # path('login/', CustomLoginView.as_view(), name='login'), 
    # path('logout/', LogoutView.as_view(), name='logout'), 
    # path('news/', NewsPageView.as_view(), name='news'), 
    # path('contact/', ContactUsPageView.as_view(), name='contact'), 
    # path('ourmission/', OurMissionPageView.as_view(), name='ourmission'), 
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('contact-us/', contact_us, name="contact_us"),
    path('our-mission/', our_mission, name="our_mission"),
    path('login/', login, name="login"),
    path('news/', NewsPageView.as_view(), name='news')
]