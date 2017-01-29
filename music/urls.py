from django.conf.urls import url
from . import views


app_name='music'
 
urlpatterns = [
    # /music/ Is the default path for this index page so you can leave the search field empty
    url(r'^$', views.IndexView.as_view(), name='index'), #  url(r'^  Everything in here is the search field  $',
    
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    
       # /music/<pk>/      # Using a class requires you to tell it to use it as_view() which means use the method of the class
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  # The (?P<pk>[0-9]+)/ is the id of the song 
    
    url(r'^(?P<pk>[\w.@+-]+)/$', views.DetailView.as_view(), name='detail'),
    
    #music/album/add/ 
    url(r'album/add/$',views.AlbumCreate.as_view(), name='album-add'),
    #I think you only use the ^ (carrot) as a placeholder when the input is a variable or does not exist, aka index
    
    url(r'song/(?P<pk>[0-9]+)/$',views.SongCreate.as_view(), name='song-add'),
    
    #music/album/pk
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
    
    
    #music/album/pk/Delete
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),
    # I think the delete button form is sending the id
    
   #My rigged home page
    url(r'^home$',views.home, name="home"),
]