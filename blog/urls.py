from django.urls import path
from . import views


urlpatterns = [
    path("", views.post, name="posts"),
    path("post/<int:pk>", views.post_detail, name="post"),
    path("category/<int:id>/", views.category_detail, name="category_detail"),
]
