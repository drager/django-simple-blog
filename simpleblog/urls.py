from django.conf.urls import url

from .views import BlogDetailView, BlogListView, LatestEntriesFeed

urlpatterns = [
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
                url(r'^$', BlogListView.as_view(), name='blog_index'),
            ]
