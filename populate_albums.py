import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','barandalla.settings')
import django
django.setup()
import subprocess
from django.core.files.images import ImageFile
from unidecode import unidecode
from gallery.models import Image, Album


album_names = ["Paisaje Localizado", "Paisaje Imaginario", "Vida Urbana", "Metrópolis", "Abstracto Temático", "Solicitudes"] #Just change this one!
album_dirs = ["images/" + unidecode(a.lower().replace(" ", "_")) + "/" for a in album_names]


def file_list(album_dir):
    command = "ls " + album_dir + " --full-time -i | sort -u"
    stdout = subprocess.check_output(command, shell=True)
    full_lines = stdout.decode().splitlines()[:-1]
    lst = []
    for l in full_lines:
        filename = l.split(" +0000 ")[1]
        if not filename.endswith(".txt"): lst.append(album_dir + filename)
    return lst


def populate(album_name, album_dir):
    print("album_name = '" + album_name + "'\nalbum_dir  = '" + album_dir + "'")
    try:
        album = Album.objects.get_or_create(name=album_name)[0]
    except:
        print("Couldn't get or create album '" + album_name + "'!")
        return

    filenames = file_list(album_dir)
    if not filenames:
        print("No filenames found. Does " + album_dir + " contain any images?") 
        print("Album will keep default or previous cover image.")
        return

    with open(filenames[0], 'rb') as f:
        album.cover = ImageFile(f)
        album.save()

    print(album.__repr__(), "..... OK")


if __name__ == '__main__':
    print("===============================================================")
    for album_name, album_dir in zip(reversed(album_names), reversed(album_dirs)):
        populate(album_name, album_dir)
        print("===============================================================")
