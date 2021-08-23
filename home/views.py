from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from .forms import LoginForm

# Create your views here.

class LoginView(FormView):
    template_name = 'views/auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('registro:informes')

    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home:home'))
        return super(FormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        print(form.get_user())
        return super(LoginView, self).form_valid(form)

class HomeView(TemplateView):
    template_name = 'views/home/index.html'

class LogoutView(FormView):

    def logout_request(request):
        logout(request)
        return super(LoginView)