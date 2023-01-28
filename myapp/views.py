from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, RedirectView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Person
from .forms import FirstForm
from django.views.generic import FormView
from django.urls import reverse_lazy
# from django.views import Views
from django.http import HttpResponse, HttpRequest
from django.contrib import messages

# トップ page
class TopView(TemplateView):
    template_name = 'top.html'
    
class IndexSecondView(TemplateView):
    template_name = 'pages/second.html'

# 一覧 page   
class IndexListView(LoginRequiredMixin, ListView):
    model = Person
    template_name = 'pages/list.html'
    paginate_by = 4
    
    def get_queryset(self):
        person = Person.objects.filter(user=self.request.user).order_by('-created_at')
        return person

# 詳細ページ
class IndexDetailView(LoginRequiredMixin, DetailView,):
    model = Person
    template_name = 'pages/detail.html'
    paginate_by = 5


# 削除ページ
class IndexDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('myapp:list')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# 変更ページ   
class IndexUpdateView(UpdateView):
    model = Person
    # fields = '__all__'
    template_name = 'pages/update.html'
    form_class = FirstForm
    
    def get_success_url(self):
        return reverse_lazy('myapp:detail', kwargs={'pk':self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, '登録データを更新しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '登録データの更新が失敗しました')
        return super().form_invalid(form)
    
    
###################################################################
    
#入力ページ
class FirstInputView(LoginRequiredMixin, CreateView):
    model = Person
    template_name = 'pages/firstinput.html'
    form_class = FirstForm
    success_url = reverse_lazy('myapp:list')
    
    def form_valid(self, form):  
        person = form.save(commit=False)
        person.user = self.request.user
        person.save()
        messages.info(self.request, '登録データを入力しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '登録データが入力できません')
        return super().form_invalid(form)
    

    






        

    




