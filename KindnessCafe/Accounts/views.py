from django.views.generic import TemplateView
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import LoginAjaxMixin
from django.contrib.auth.views import LoginView
from bootstrap_modal_forms.generic import BSModalLoginView


from django.views.generic.edit import FormView #temp
from .forms import CustomUserCreationForm #temp

class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactUsPageView(TemplateView):
	template_name = 'contact.html'



class SignupPageView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
	template_name = 'signup.html'
	form_class = CustomUserCreationForm
	success_message = 'Success: You were successfully logged in.'
	extra_context = dict(success_url=reverse_lazy('index'))

	def form_valid(self, form):
		form.send_email()
		return super(SignupPageView, self).form_valid(form)




class Index(TemplateView):
	model = User
	ctx_obj_name = 'user'
	template_name = 'index.html'



class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')


 
class OurMissionPageView(TemplateView):
	template_name = 'ourmission.html'