try:
    from django.urls import re_path as u
except ModuleNotFoundError as e:
    from django.conf.urls import url as u


from .views import BlogDetailView, BlogListView, LatestEntriesFeed


urlpatterns = [
    u(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-_\w]+)/$',
      BlogDetailView.as_view(),
      name='blog_detail'
    ),
    u(r'^archive/$',
      BlogListView.as_view(
      template_name="simpleblog/post_archive.html",
      page_template="simpleblog/post_archive_page.html"),
      name="blog_archive"
    ),
    u(r'^latest/feed/$', LatestEntriesFeed()),
    u(r'^$', BlogListView.as_view(), name='blog_index')
]

