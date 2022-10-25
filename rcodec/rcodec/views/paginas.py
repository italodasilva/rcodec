from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


@login_required
def pagina1(request):
    return render(request, 'core/pagina1.html', {})

@login_required
def pagina2(request):
    return render(request, 'core/pagina2.html', {})
