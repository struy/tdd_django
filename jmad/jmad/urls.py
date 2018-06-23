from django.conf.urls import include, url
from django.contrib import admin
from solos.views import solo_detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'jmad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'solos.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>\[\w-]+)/$', 'solos.views.solo_detail', name='solo_detail_view'),
]
