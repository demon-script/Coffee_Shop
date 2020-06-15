from django.urls import path
from core import views as core_views

#create here the Views
urlpatterns = [
                path('',core_views.index,name = 'index'),
                path('about/',core_views.about,name = 'nosotros'),
                path('services/',core_views.services,name = 'servicios'),
                path('store/',core_views.store,name = 'tienda'),
                path('contact/',core_views.conctac,name = 'contacto'),
                path('infoblog/',core_views.blog,name = 'blog'),
                path('sample/',core_views.samples,name = 'prueba'),
            ]