from django import forms
from .models import UsuarioTipo, Pais, Region, Usuario, DocumentoTipo

class UsuarioTipoForm(forms.ModelForm):
    class Meta:
        model = UsuarioTipo
        fields = ['id_usuario_tipo', 'usuario_tipo']

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['id_pais', 'pais']

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['id_region', 'region']

class DocumentoTipoForm(forms.ModelForm):
    class Meta:
        model = DocumentoTipo
        fields = ['id_documento_tipo', 'documento_tipo']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'id_usuario_tipo', 'usuario_nombre', 'usuario_apellido', 'telefono', 'email', 'direccion', 'id_region', 'id_pais']