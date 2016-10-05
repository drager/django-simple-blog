from django.db.models.signals import post_save

from .models import Comment, Post


def save_comment(sender, instance, created, **kwargs):
    if created:
        comment = instance
        post = comment.post
        post.comment_count = post.comments.count()
        post.save(force_update=True)
