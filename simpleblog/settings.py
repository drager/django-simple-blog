"""
Django Simple Blog settings file.
"""

from django.conf import settings

# How long the length of the textarea should be.
MAX_LENGTH_TEXTAREA = getattr(settings, 'BLOG_MAX_LENGTH_TEXTAREA', None)
BLOG_LIST_MAX_PREV_WORDS = getattr(settings, 'BLOG_LIST_MAX_PREV_WORDS', 10)
