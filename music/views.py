from django.views import generic #Need to watch a tutorial on this module
#Request and Generic are setup to check the template folder for html pages
from django.shortcuts import render, redirect # redirects you to a new page
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login # authenticate takes the username and pass and makes sure they are existing members. 
# logging gives a person a special id while browsing the website so they don't have to login on every page
from django.views.generic import View
from .forms import UserForm # This is importing the class UserForm we created in forms
from .models import Album,Song
from django.db.transaction import commit
from django.db import models
from django import forms



# The generic.ListView takes a list of items or a class and it's attributes (and maybe a dictionary?) puts it into a variable and sends it to the path
class IndexView(generic.ListView): # This is the list generic view
    template_name = "music/index.html" # This is the html page you want to send this data to
# object_list is the variable that the class generic.ListViews uses to send it's data
    context_object_name = "all_albums" 
#The above line changes object_list to  all_albums So now you can use all_albums as a variable instead of object_list
    def get_queryset(self): # get_queryset has to be that name or it doesn't work
        return Album.objects.all()

#The generic.DetailView takes an object and sends it to the path as its own name in this case the Album class
class DetailView(generic.DetailView): # This is the single item generic view
    model = Album  # This is saying that you want to look at the Album class for your data
    template_name = 'music/detail.html' # This is the html page you want to send this data to
    
def home(request):  
#This is my home page i rigged together  
    return render(request, 'music/Home.html')  # Render does what it sounds like it is rendering the home html

# This is creating the ability for a user to create a Album
#This class looks for a lower case name of the model= from below in  template model _form.html for a form page. example album_form in the templates folder
class AlbumCreate(CreateView): #Is a premade create function imported from Django
#This create method generates a form field with the data from the model. The class attributes will be labels on the left and the to the right of each label will be a input field. 
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo'] #This is a list
# You need to specify which fields of the specified class you want people to be able to fill out from the 
# website when creating a Album


#===============================================================================
# Study this 

class SongCreate(CreateView):
    model = Song
    fields = ['file_type', 'song_title']
                                                        
    def form_valid(self, form):
            form.instance.album = Album.objects.get(pk=self.kwargs['pk'])
            return super(SongCreate, self).form_valid(form)
    
                                                         
    # name_of_song.album = Album.object.get(pk=2) Is literally the only way i know how to assign a song to a album
    # So (pk=2) needs to become dynamic inputing the pk of the page you are on
#===============================================================================
    
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    #I think the delete button form is sending the album.id
    model = Album
    success_url = reverse_lazy('music:index') #This is where you will be redirected after deletion

class UserFormView(View):
    form_class = UserForm # you need to make form_class= to the class you created in forms that you want to use
    template_name = 'music/registration_form.html' # template_name needs to be set to the _form you made 
    # in templates/music but you don't need to add templates/ since it is set up to auto look/start in the templates folder
    
    # I think when you make a form in html and the method=get it is actually calling a method called get
    # so i think we are making this get to be activated by that method? or at least when using these View classes 
    #it seems to be the case
    def get(self,request): # self is the UserFormView class
        form = self.form_class(None)  # This is the blank form to be filled out so you are not requesting any data so it is None
        return render(request,self.template_name, {'form':form}) # here you are requesting the  template_name variable from above and 'form':form data to be passed to the page
    # self.template_name is the attribute for the class we created above which is basically the page.html "form":form is just the default form sheet                                                                                                                                                       
    
    def post(self, request):
        form = self.form_class(request.POST) # when someone hits submit on a form button POST contains the data that was filled in so this is requesting for that data
        
        if form.is_valid(): # this is in case they tried to use a illegal character in their input fields
            
            user = form.save(commit=False) # This is saving the form data to a variable but not to the database so a user is not created yet aka commit=False
            # we do this so we can make any needed alterations to the information before it is dedicated to the database like formating 
           
            # clean (normalized) data that is formated properly like formating the date patterns 1/17/2017
            username = form.cleaned_data["username"] # username and password are stored in the POST you requested since they where in the form fields 
            password = form.cleaned_data['password']   # formats the data to some specifications I'm not clear on but apparently is needed.
            # At this point i believe the password is still text but  once set it becomes scrambled in a unreadable hash
            
            user.set_password(password) # password is now set and unreadable
            user.save() # user has now been saved to the database
            
                
    # Returns user objects if credentials are correct
            user = authenticate(username=username, password=password)
                                                  #field           variable       field            variable
            if user is not None:
                
                if user.is_active:
                    
                    login(request, user)
                    return redirect('music:index')
    
    
        return render(request,self.template_name, {'form':form})       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







