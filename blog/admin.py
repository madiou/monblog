# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'approved')
    list_filter = ('approved', 'date_posted', 'author')
    search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ('name', 'email', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

