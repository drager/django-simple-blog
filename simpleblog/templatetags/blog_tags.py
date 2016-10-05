from django import template

from ..models import Post

register = template.Library()


def latest_blog_posts(context, num):
    """
    Displays the most recent blog posts. It takes an argument, num
    and displays so many posts depending on the value.
    """
    latest_blog_posts = Post.objects.all()[:num].select_related()

    return {
        'latest_blog_posts': latest_blog_posts
    }

register.inclusion_tag('tags/latest_blog_posts.html',
                       takes_context=True)(latest_blog_posts)
