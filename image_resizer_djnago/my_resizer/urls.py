from django.urls import path
from my_resizer.views import index


urlpatterns = [
    path('', index, name='index')
]
