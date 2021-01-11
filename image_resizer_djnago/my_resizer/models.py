from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class ImageResizerClass(models.Model):
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    FILE_TYPE_CHOICES = (
        ("byte", "Byte"),
        ('kb', 'KB'),
        ('mb', 'MB')
    )
    file_size_type = models.CharField(max_length=7, choices=FILE_TYPE_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='resized_images/')
    
    # def save(self, *args, **kwargs):
    #     super().save()
    #     img = Image.open(self.image.path)

    #     print(img.height)
    #     print(img.width)


    # def save(self, *args, **kwargs):
    #     # Opening the uploaded image
    #     img = Image.open(self.image)

    #     if img.height > 200 or img.width > 200:

    #         output_size = (200, 200)
    #         img.thumbnail(output_size)
    #         img = img.convert('RGB')

    #         output = BytesIO()
    #         img.save(output, format='JPEG')
    #         output.seek(0)

    #         # change the imagefield value to be the newley modifed image value
    #         self.image = InMemoryUploadedFile(output, 'ImageField',
    #                                         f'{self.image.name.split(".")[0]}.jpg',
    #                                         'image/jpeg', sys.getsizeof(output),
    #                                         None)

    #         super().save(*args, **kwargs)
#


