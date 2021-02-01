from django.urls import path
from .views import (ArticleCreateView, ArticleDeleteView, ArticleDetailView,
ArticleListView, ArticleUpdateView, CategoryArticleListView)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='update-article'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='delete-article'),
    path('create/', ArticleCreateView.as_view(), name='create-article'),
    path('<category>/', CategoryArticleListView.as_view(), name='articles-category'),
]