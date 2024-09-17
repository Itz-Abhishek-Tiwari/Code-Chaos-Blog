from django.shortcuts import get_object_or_404, render
from .models import Post, Categories


def post(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post.html", {"post": post})


def category_detail(request, id):
    category = get_object_or_404(Categories, id=id)
    posts = category.post_type.all()  # Fetch posts related to the category
    return render(
        request, "blog/category_detail.html", {"category": category, "posts": posts}
    )
