from articles import views
from django.urls import path

urlpatterns = [
    path("", views.ArticleView.as_view(), name="todolist"),
]
