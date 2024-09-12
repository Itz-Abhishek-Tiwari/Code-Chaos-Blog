from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Post(models.Model):
    BLOG_TYPE = [
        ("ML", "Machine Learning"),
        ("JS", "Java Script"),
        ("PY", "Python"),
        ("AI", "Artifical Inteligence"),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    type = models.CharField(max_length=2, choices=BLOG_TYPE, null=True, blank=True)

    def __str__(self):
        return self.title


# One To Many


class PostReview(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(null=True, blank=True)
    data_added = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return f"{self.user.username} reviews for {self.post.title}"


# Many to Many
class Categories(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    post_type = models.ManyToManyField(Post, related_name="categories")

    def __str__(self):
        return self.name


# One To One


class PostCertificate(models.Model):
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"certificate for {self.post}"
