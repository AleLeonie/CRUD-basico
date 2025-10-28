"""
Superusuario informaciòn
    Username: inacap
    Email Address:
    Password: inacap
"""
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (
    Pais,
    Region,
    UsuarioTipo,
    Usuario,
    DocumentoTipo,
    Documento
)


class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'pais')
    search_fields = ('id_pais', 'pais')
    ordering = ('pais',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'region')
    search_fields = ('id_region', 'region')
    ordering = ('region',)


class UsuarioTipoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario_tipo', 'usuario_tipo')
    search_fields = ('id_usuario_tipo', 'usuario_tipo')
    ordering = ('usuario_tipo',)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id_usuario',
        'usuario_nombre',
        'usuario_apellido',
        'id_usuario_tipo',
        'id_pais',
        'id_region',
        'email',
        'telefono'
    )
    search_fields = ('id_usuario', 'usuario_nombre', 'usuario_apellido', 'email')
    list_filter = ('id_usuario_tipo', 'id_pais', 'id_region')
    ordering = ('usuario_nombre', 'usuario_apellido')


class DocumentoTipoAdmin(admin.ModelAdmin):
    list_display = ('id_documento_tipo', 'documento_tipo')
    search_fields = ('id_documento_tipo', 'documento_tipo')
    ordering = ('documento_tipo',)


class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'id_documento',
        'documento_nombre',
        'id_usuario',
        'id_documento_tipo'
    )
    search_fields = ('id_documento', 'documento_nombre', 'id_usuario__usuario_nombre', 'id_usuario__usuario_apellido')
    list_filter = ('id_documento_tipo',)
    ordering = ('documento_nombre',)


# Registro de modelos con admin.site.register()
admin.site.register(Pais, PaisAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(UsuarioTipo, UsuarioTipoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(DocumentoTipo, DocumentoTipoAdmin)
admin.site.register(Documento, DocumentoAdmin)
