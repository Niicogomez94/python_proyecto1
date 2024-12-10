from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicacion Django 2"}
    return render(request, "myapp/index.html", context)
