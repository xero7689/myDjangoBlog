from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<slug>[\w\-]+)/$', 'views.post'),
    url(r'^tags/(?P<tagName>[\w\-]+)/$', 'views.tag'),
    url(r'^taglist/$', views.tagList.as_view()),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.ContactView.as_view()),
    url(r'^contactSuccess/$', 'views.ContactSuccess'),
    url(r'^archive/$', views.archiveList.as_view()),
    
    #Unused
    #url(r'^(?P<year>\d{4})/$', ArticleYearArchiveView.as_view(),name="article_year_archive"),
    #url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', ArticleMonthArchiveView.as_view(month_format='%m'), name="archive_month_numeric"),
)
