from django.shortcuts import get_object_or_404, redirect, render
from rcodec.models import *
from django.forms import ModelForm

class RepositorioForm(ModelForm):
    class Meta:
        model = Repositorio
        fields = '__all__'

def listar(request):
    repositorio =  Repositorio.objects.all()

    return render(request, 'core/pagina1.html', {
        'repositorio': repositorio
    })


def criar(request):
    frm = RepositorioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('repositorio')

    return render(request, 'core/pagina2.html',{
        'titulo' : 'Enviar Arquivo',
        'frm':frm
    })

def editar(request,id):
    repositorio = get_object_or_404(Repositorio, pk=id)
    frm = RepositorioForm(request.POST or None, instance=repositorio)

    if frm.is_valid():
        frm.save()
        return redirect('repositorio')

    return render(request, 'core/pagina2.html',{
        'titulo' : 'Editar Arquivo',
        'frm':frm
    })

def excluir(request,id):
    repositorio = get_object_or_404(Repositorio, pk=id)
    repositorio.delete()

    return redirect('repositorio')