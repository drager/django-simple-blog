from django.conf.urls import patterns, url

from .views import BlogListView, BlogDetailView, LatestEntriesFeed

urlpatterns = patterns('simpleblog.views',
                       url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-_\w]+)/$',
                           BlogDetailView.as_view(),
                           name='blog_detail',
                           ),
                       url(r'^archive/$',
                           BlogListView.as_view(
                               template_name="simpleblog/post_archive.html",
                               page_template="simpleblog/post_archive_page.html"),
                           name="blog_archive"),
                       url(r'^latest/feed/$', LatestEntriesFeed()),
                       )
