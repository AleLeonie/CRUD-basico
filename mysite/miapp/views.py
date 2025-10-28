from django.shortcuts import render, redirect, get_object_or_404

from .models import UsuarioTipo, Pais
from .forms import UsuarioTipoForm, PaisForm

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

def usuario_tipo_delete(request, id_usuario_tipo):
    usuario_tipo = get_object_or_404(UsuarioTipo, id_usuario_tipo=id_usuario_tipo)
    usuario_tipo.delete()
    return redirect('usuarios_tipos_lista')

# Funciones Pais
def paises_lista(request):
    paises = Pais.objects.all()
    return render(request, 'usuario/paises.html', {'paies':paises})

def pais_create(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paises_lista')
    else:
        form = PaisForm()

    return render(request, 'usuario/paises_form.html', {'form': form})

def pais_delete(request, id_pais):
    pais = get_object_or_404(Pais, id_pais=id_pais)
    pais.delete()
    return redirect('paises_lista')

# Funciones Region



# Funciones Usuario