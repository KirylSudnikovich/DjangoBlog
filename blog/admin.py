from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'created_date', 'published_date']
    list_filter = ['created_date', 'published_date']
    search_fields = ['title']
    inlines = [CommentInline]