from django import forms
from .models import UsuarioTipo, Pais, Region

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