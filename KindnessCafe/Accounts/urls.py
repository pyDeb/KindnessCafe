from django.urls import path
# from .views import HomePageView, SignupPageView, Index, CustomLoginView, ContactUsPageView, OurMissionPageView 
from .views import index, contact_us, our_mission, login_view, signup, logout_view, recruitment_view
from News.views import news_view

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
    path('login/', login_view, name="login"),
    path('news/', news_view, name='news'),
    path('logout/', logout_view, name='logout'),
    path('recruitment/', recruitment_view, name='recruitment'),
]