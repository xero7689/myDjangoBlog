from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from blog.views import archiveList, tagList, work, ContactView, ContactSuccess, ArticleYearArchiveView, ArticleMonthArchiveView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),	# "^$" means blank
    url(r'^posts/(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r'^tags/(?P<tagName>[\w\-]+)/$', 'blog.views.tag'),
    url(r'^taglist/$', tagList.as_view()),
    url(r'^about/$', 'blog.views.about'),
    url(r'^work/$', work.as_view()),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^contactSuccess/$', 'blog.views.ContactSuccess'),
    url(r'^archive/$', archiveList.as_view()),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^(?P<year>\d{4})/$',ArticleYearArchiveView.as_view(),name="article_year_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', ArticleMonthArchiveView.as_view(month_format='%m'), name="archive_month_numeric"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
