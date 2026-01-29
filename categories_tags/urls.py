from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("category/<slug:slug>/",views.CategoryPostListView.as_view(),name="category-posts"),
    path("categories/",views.CategoryListView.as_view(),name="category-index"),
]