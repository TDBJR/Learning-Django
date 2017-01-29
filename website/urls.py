from django.conf.urls import include, url
from django.contrib import admin
from . import  views #<--------importing from this directory not musics
#Below are the imports from the settings that control the media upload save location additions
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$',views.index, name="home"),  #<---referring to this folders index not musics.
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
]

#This is saying if we are in DEBUG and not production we will save the uploaded media to our defined location in settings which is in the 
#"/media/" folder. In production you will want to save it to a server.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)