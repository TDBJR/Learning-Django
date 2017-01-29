from django.db import models
from django.core.urlresolvers import reverse 

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField() # You need to add a path to upload to in settings.py
    
    def get_absolute_url(self):
        #This is going to be used by the add Album button to redirect to music/pk number
        return reverse('music:detail', kwargs={'pk':self.pk})# kwargs = key word argument. pk is a hidden attribute of all classes and is also known as id
        # I think this is saying that on creating a Album you want it to redirect you to the newly created Album page                                            
    def __str__(self):
        return self.album_title + '-' + self.artist
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) # This is the Album object it is linked to
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.album.id})# self.album_id is the Album object so it returns the Album object that is tied to the ForeinKey. for example 
# {<Album: Recovery-Eminem>} which is why you need to add .id
    
    def __str__(self):
        return self.song_title
    
    
    
   
     
    
    
    