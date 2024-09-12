from django.contrib import admin
from .models import Post, PostReview, Categories, PostCertificate


class PostReviewInline(admin.TabularInline):
    model = PostReview
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "published_date")
    inlines = [PostReviewInline]


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("post_type",)


class PostCertificateAdmin(admin.ModelAdmin):
    list_display = ("post", "certificate_number")


admin.site.register(Post, PostAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(PostCertificate, PostCertificateAdmin)
