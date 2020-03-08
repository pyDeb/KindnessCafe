from django.views.generic import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.models import User


from bootstrap_modal_forms.generic import BSModalLoginView


class HomePageView(TemplateView):
    template_name = 'home.html'




class Index(TemplateView):
	model = User
	ctx_obj_name = 'user'
	template_name = 'index.html'



class SignupPageView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_message = 'Success: Sign up succeeded. You can now Log in.'
	success_url = reverse_lazy('index')



class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')


 