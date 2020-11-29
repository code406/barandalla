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
    #i = 1 #ON-DL
    for l in full_lines:
        filename = l.split(" +0000 ")[1]
        if not filename.endswith(".txt"): 
            new_name = album_dir + filename
            #new_name = album_dir + str(i).zfill(4) + ".jpg" #ON-DL
            #os.rename(album_dir + filename, new_name) #ON-DL
            lst.append(new_name)
            #i+=1 #ON-DL
    return lst


def populate(album_name, album_dir):
    print("album_name = '" + album_name + "'\nalbum_dir  = '" + album_dir + "'")
    try:
        album = Album.objects.filter(name=album_name)[0]
    except:
        print("There is no album called '" + album_name + "'!")
        return
    Image.objects.filter(tag=album).delete() # REMOVE THE DELETO IN REAL V (!!!)
    with open(album_dir + "image_info.txt", 'r') as in_file:
        lines = [line for line in in_file.readlines() if line.strip()]
    
    filenames = file_list(album_dir)
    if not filenames:
        print("No filenames found. Does " + album_dir + " contain any images?") 
        return

    for i, line in enumerate(lines):
        s = []
        splet = list(filter(None, line.split('  ')))
        for sp in splet: 
            s.append(sp.strip())
        disp = True if s[4]=="Disponible" else False

        image = Image(name=s[1], details=s[3], size=s[2], disp=disp, tag=album)
        with open(filenames[i], 'rb') as f:
            image.image = ImageFile(f)
            image.save()

        print(image.__repr__())


if __name__ == '__main__':
    print("===============================================================")
    for album_name, album_dir in zip(album_names, album_dirs):
        populate(album_name, album_dir)
        print("===============================================================")