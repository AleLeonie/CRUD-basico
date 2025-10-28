from django.urls import path
from . import views
from .views import usuarios_tipos_lista, usuario_tipo_create, paises_lista, pais_create, regiones_lista, region_create

urlpatterns = [
    path('index/', views.index, name='index'),

    # URLs Usuario Tipo
    path('usuario/usuariostipos/', usuarios_tipos_lista, name='usuarios_tipos_lista'),
    path('usuario/crearusuariostipos/', usuario_tipo_create, name='usuario_tipo_create'),
    path('usuario/usuariostipos/eliminar/<str:id_usuario_tipo>/', views.usuario_tipo_delete, name='usuario_tipo_delete'),
    
    # URLs Pais
    path('usuario/paises/', paises_lista, name='paises_lista'),
    path('usuario/crearpaises', pais_create, name='pais_create'),
    path('usuario/paises/eliminar/<str:id_pais>/', views.pais_delete, name='pais_delete'),

    # URLS Region
    path('usuario/regiones/', regiones_lista, name='regiones_lista'),
    path('usuario/crearregiones', region_create, name='region_create'),
    path('usuario/regiones/eliminar/<str:id_region>/', views.region_delete, name='region_delete'),
]