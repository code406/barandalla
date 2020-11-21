from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:album_id>/', views.album, name='album'),
    path('contacto/', views.contact, name='contact'),
]