"""
Django Simple Blog settings file.
"""

from django.conf import settings

# How long the length of the textarea should be.
MAX_LENGTH_TEXTAREA = getattr(settings, 'BLOG_MAX_LENGTH_TEXTAREA', None)
PREVIEW_WORDS_COUNT = getattr(settings, 'BLOG_PREVIEW_WORDS_COUNT', None)
