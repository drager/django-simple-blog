from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'post_date', 'posted_by',
                    'comment_count', 'allow_comments')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'ip_address', 'post_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
