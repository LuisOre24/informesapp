from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from .forms import LoginForm

# Create your views here.

class LoginView(FormView):
    template_name = 'views/auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:home')

    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print('login ok')
            return redirect(reverse_lazy('home:home'))
        print('filed')
        print(request.user)
        return super(FormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        print('login')
        print(f'{form.get_user()}')
        return super(LoginView, self).form_valid(form)

class HomeView(TemplateView):
    template_name = 'views/home/index.html'
