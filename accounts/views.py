from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import SignupForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

# signup page
class SignUpView(CreateView):
    template_name = 'accounts/signup.html' 
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')
    def form_valid(self, form):
        messages.success(self.request, '新規登録')
        return super().form_valid(form) 
# login page
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    # authentication_form = UserLoginForm
    
    def form_valid(self, form):
        messages.success(self.request, 'ログインしました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'エラーでログインできませんでした。')
        return super().form_invalid(form) 
    
class UserLogoutView(LogoutView):
    pass

