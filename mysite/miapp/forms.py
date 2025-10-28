from django import forms
from .models import UsuarioTipo, Pais, Region, DocumentoTipo

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