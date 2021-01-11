from django.urls import path
from my_resizer.views import index, save_data
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'), 
    path('save_data', save_data, name='save_data')
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)