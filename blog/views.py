from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

from .models import Article, Category
from .forms import ArticleModelForm

class ArticleListView(ListView):
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleModelForm

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("blog:articles")


class CategoryArticleListView(ListView):

    template_name = 'blog/article_list.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Article.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context