from django.shortcuts import render, redirect
from .models import ImageResizerClass
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from io import BytesIO
import os
import cv2

path = ""

def index(request):
    return render(request, 'index.html')


def save_data(request):
    global path

    print('path', path)

    # delete image
    if path != "":
        os.remove(path)
        
    # collect the data
    height = request.POST['height']
    width = request.POST['width']
    img = request.FILES['img']

    # create object
    x = ImageResizerClass.objects.create(image=img)

    # gobal path
    path = 'media/{}'.format(x.image)
    
    # resize image
    imgs = cv2.imread(path)
    imgs = cv2.resize(imgs,(int(width),int(height)))
    cv2.imwrite(path,imgs)

    # get image
    id = x.id
    img_obj = ImageResizerClass.objects.get(id=id)
    temp = img_obj
    
    # delete object from database
    img_obj.delete()


    # imgs = Image.open(img)
    #output_size = (200, 200)
    #imgs.thumbnail(output_size)
    #imgs = imgs.convert('RGB')
    
    # #output = BytesIO()
    # imgs.save(output, format='JPEG')
    # output.seek(0)

    # img = InMemoryUploadedFile(output,'ImageField',
    #                                         f'{img.name.split(".")[0]}.jpg',
    #                                         'image/jpeg',sys.getsizeof(output),
    #                                         None)


    
    return render(request, 'download.html', {'img': temp})
