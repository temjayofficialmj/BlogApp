from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogList(ListView):
	model = Post
	template_name = 'home.html'

class BlogDetail(DetailView):
	model = Post
	template_name = 'post_detail.html'

class BlogCreate(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = '__all__'
	success_url = reverse_lazy('home')

class BlogUpdate(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']
	success_url = reverse_lazy('home')

class BlogDelete(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')