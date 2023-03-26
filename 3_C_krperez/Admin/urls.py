
from django.urls import path
from django import views
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    
     path('index', views.index,name='index'),
     path('eliminar/<int:id>', views.eliminar,name='eliminar'),
     path('agregar', views.agregar,name='agregar'),
     path('listar', views.listar,name='listar'),
     path('crear', views.crear,name='crear'),
     path('', views.logear,name='logear'),
     path('editar/<int:id>', views.editar,name='editar'),
     path('cerrar_sesion',views.cerrar_sesion, name="cerrar_sesion"),
     path('edimagen/<int:id>',views.edimagen, name="edimagen"),
     path('list',views.list, name="list"),
     path('imagenedi/<int:id>',views.imagenedi, name="imagenedi"),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
