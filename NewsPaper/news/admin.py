from django.contrib import admin

from .models import Post, PostCategory, Author, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'header')


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
