from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from gallery.models import Image, Album
from gallery.forms import ImageForm

#TODO: Change to receive slug instead of album_id
def album(request, album_id=0):
    images = []
    album_name = "¡Vaya! Esta página no existe."
    if album_id == 0:
        images = Image.objects.all().reverse()
        album_name = "Todo"
    else:
        albums = Album.objects.filter(id=album_id)
        if albums:
            images = Image.objects.filter(tag=albums[0])
            album_name = albums[0].name
    #return render(request, 'gallery.html', {'images': images})
    return render(request, 'album.html', {'images': images, 'album_name': album_name})

def index(request):
    albums = Album.objects.all().order_by('-id')
    return render(request, 'index.html', {'albums': albums})

def contact(request):
    return render(request, 'contact.html')
