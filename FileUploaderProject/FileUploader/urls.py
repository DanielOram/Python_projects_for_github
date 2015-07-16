__author__ = 'danieloram'

from django.conf.urls import patterns, url
#extra import stuff
from django.conf.urls.static import static
from django.conf import settings
#root page and redirect page
urlpatterns = patterns('FileUploader.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^image', 'images', name='images'),
    #url pattern for displaying uploaded images in there own tab. needs a special pattern for the files location in media.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)