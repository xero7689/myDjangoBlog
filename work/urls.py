from django.conf.urls import patterns, include, url
from work import views

urlpatterns = patterns('',
    url(r'/work/', views.work.as_view()),
)

