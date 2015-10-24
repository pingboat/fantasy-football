from django.conf.urls import patterns, include, url
from django.contrib import admin
from football import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^search/results/$', views.results),
    url(r'^scoreboard/$', views.scoreboard),
    url(r'^scoreboard/(\d{1,2})/$', views.previous_scoreboard),
    url(r'^team/(\d{1})/$', views.team),
    url(r'^team/new/$', views.new_team),
    
    # url(r'^admin/', include(admin.site.urls)),
)
