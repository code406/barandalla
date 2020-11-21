from django.contrib import admin
from django.contrib.auth.models import Group
from gallery.models import Image, Album

admin.site.unregister(Group)
admin.site.register(Image)
admin.site.register(Album)
