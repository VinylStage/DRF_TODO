from articles import views
from django.urls import path

urlpatterns = [
    path("", views.ArticleView.as_view(), name="todolist"),
    path("post/", views.ArticleCreateView.as_view(), name="todopost"),
    path("detail/<int:pk>/", views.ArticleDetailView.as_view(), name="tododetail"),
    path("delete/<int:pk>/", views.ArticleDetailView.as_view(), name="delete"),
]
