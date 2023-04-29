from articles import views
from django.urls import path

urlpatterns = [
    path("todolist/", views.ArticleView.as_view(), name="todolist"),
]
