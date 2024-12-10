from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicacion Django 2"}
    return render(request, "myapp/index.html", context)

from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm

def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/exito.html')  # Crea esta plantilla
    else:
        form = PostForm()
    return render(request, 'myapp/agregar_post.html', {'form': form})

def buscar_post(request):
    query = request.GET.get('q', '')
    resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'myapp/buscar_post.html', {'resultados': resultados, 'query': query})

