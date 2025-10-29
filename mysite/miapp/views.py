from django.shortcuts import render, redirect, get_object_or_404

from .models import UsuarioTipo, Pais, Region, Usuario, DocumentoTipo
from .forms import UsuarioTipoForm, PaisForm, RegionForm, UsuarioForm, DocumentoTipoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Funciones Usuario Tipo
def usuarios_tipos_lista(request):
    usuarios_tipos = UsuarioTipo.objects.all()
    return render(request, 'usuario/usuariostipos.html', {'usuariostipos': usuarios_tipos})

def usuario_tipo_create(request):
    if request.method == 'POST':
        form = UsuarioTipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_tipos_lista')
    else:
        form = UsuarioTipoForm()
    
    return render(request, 'usuario/usuariostipos_form.html', {'form': form})

def usuario_tipo_update(request, id_usuario_tipo):
    usuario_tipo = get_object_or_404(UsuarioTipo, id_usuario_tipo=id_usuario_tipo)
    if request.method == 'POST':
        form = UsuarioTipoForm(request.POST, instance=usuario_tipo)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_usuario_tipo'].disabled = True
        if form.is_valid():
            form.save()
            return redirect('usuarios_tipos_lista')
    else:
        form = UsuarioTipoForm(instance=usuario_tipo)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_usuario_tipo'].disabled = True
    
    return render(request, 'usuario/usuariostipos_form.html', {'form': form})

def usuario_tipo_delete(request, id_usuario_tipo):
    usuario_tipo = get_object_or_404(UsuarioTipo, id_usuario_tipo=id_usuario_tipo)
    usuario_tipo.delete()
    return redirect('usuarios_tipos_lista')

# Funciones Pais
def paises_lista(request):
    paises = Pais.objects.all()
    return render(request, 'usuario/paises.html', {'paises':paises})

def pais_create(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paises_lista')
    else:
        form = PaisForm()

    return render(request, 'usuario/paises_form.html', {'form': form})

def pais_update(request, id_pais):
    pais = get_object_or_404(Pais, id_pais=id_pais)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_pais'].disabled = True
        if form.is_valid():
            form.save()
            return redirect('paises_lista')
    else:
        form = PaisForm(instance=pais)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_pais'].disabled = True

    return render(request, 'usuario/paises_form.html', {'form': form})

def pais_delete(request, id_pais):
    pais = get_object_or_404(Pais, id_pais=id_pais)
    pais.delete()
    return redirect('paises_lista')

# Funciones Region
def regiones_lista(request):
    regiones = Region.objects.all()
    return render(request, 'usuario/regiones.html', {'regiones':regiones})

def region_create(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regiones_lista')
    else:
        form = RegionForm()

    return render(request, 'usuario/regiones_form.html', {'form': form})

def region_update(request, id_region):
    region = get_object_or_404(Region, id_region=id_region)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_region'].disabled = True
        if form.is_valid():
            form.save()
            return redirect('regiones_lista')
    else:
        form = RegionForm(instance=region)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_region'].disabled = True

    return render(request, 'usuario/regiones_form.html', {'form': form})

def region_delete(request, id_region):
    region = get_object_or_404(Region, id_region=id_region)
    region.delete()
    return redirect('regiones_lista')

# Funciones Usuario
def usuarios_lista(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/usuarios.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_lista')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/usuario_form.html', {'form': form})

def usuario_update(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        # Deshabilitar el campo de la clave primaria
        form.fields['id_usuario'].disabled = True
        if form.is_valid():
            form.save()
            return redirect('usuarios_lista')
    else:
        form = UsuarioForm(instance=usuario)
        form.fields['id_usuario'].disabled = True  # Deshabilitar el campo de la clave primaria
    
    return render(request, 'usuario/usuario_form.html', {'form': form})

def usuario_delete(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    usuario.delete()
    return redirect('usuarios_lista')

# Funciones Documento Tipo
def documentos_tipos_lista(request):
    documentos_tipos = DocumentoTipo.objects.all()
    return render(request, 'documento/documentostipos.html', {'documentostipos': documentos_tipos})

def documento_tipo_create(request):
    if request.method == 'POST':
        form = DocumentoTipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documentos_tipos_lista')
    else:
        form = DocumentoTipoForm()
    
    return render(request, 'documento/documentostipos_form.html', {'form': form})

def documento_tipo_update(request, id_documento_tipo):
    documento_tipo = get_object_or_404(DocumentoTipo, id_documento_tipo=id_documento_tipo)
    if request.method == 'POST':
        form = DocumentoTipoForm(request.POST, instance=documento_tipo)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_documento_tipo'].disabled = True
        if form.is_valid():
            form.save()
            return redirect('documentos_tipos_lista')
    else:
        form = DocumentoTipoForm(instance=documento_tipo)
        # Deshabilitar el campo de la clave primaria para que no se pueda modificar
        form.fields['id_documento_tipo'].disabled = True

    return render(request, 'documento/documentostipos_form.html', {'form': form})

def documento_tipo_delete(request, id_documento_tipo):
    documento_tipo = get_object_or_404(DocumentoTipo, id_documento_tipo=id_documento_tipo)
    documento_tipo.delete()
    return redirect('documentos_tipos_lista')

# Funciones Documento

# Funciones Usuario