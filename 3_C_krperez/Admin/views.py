from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse ,request
from .models import Usuarios,Imagen
from .forms import creaform 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,  authenticate 
from django.contrib import messages
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates")'
    
)


def index (request):
    jds= Usuarios.objects.all()
    return render (request,"index.html", {'index': jds})

def listar (request):
    users =Usuarios.objects.all()
    datos = {'usuarios': users}
    return render(request,'crud/listar.html',datos)

def agregar (request):
    agrega= Usuarios.objects.all()
    return render (request,"index.html", {'agrega': agrega})

def actualizar (request):
    users = Usuarios.objects.all()
    datos = {'usarios': users}
    return render(request,'crud/actualizar.html' ,datos)

def eliminar (request,id):
    agrega= Usuarios.objects.get(id=id)
    agrega.delete()
    return redirect('listar')

def crear (request):
    formulario = creaform(request.POST or None , request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('listar')
    return render (request,"crud/crear.html", {'formulario': formulario})

def logear (request):
     formulario = creaform(request.POST or None , request.FILES or None)
     if formulario.is_valid():
        formulario.save()
        return redirect ('index')
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
        else:
            messages.error(request, "usuario no válido")
     else:
        messages.error(request, "información incorrecta")

        form=AuthenticationForm()
        return render(request,"Logear.html",{"form":form})
    


def editar (request,id):
    agrega=Usuarios.objects.get(id=id)
    formulario=creaform(request.POST or None , request.FILES or None ,instance=agrega)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('index')
    return render (request,"editar.html", {'formulario': formulario})

def cerrar_sesion(request):
    logear(request)
    return redirect('index')

def edimagen (request,id):
    agrega=Imagen.objects.get(id=id)
    formulario=creaform(request.POST or None , request.FILES or None ,instance=agrega)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('index')
    return render (request,"editar.html", {'formulario': formulario})

def list (request):
    user =Imagen.objects.all()
    dato = {'usuarios': user}
    return render(request,'crud/list.html',dato)


def imagenedi (request,id):
   agreg=Imagen.objects.get(id=id)
   formulari=creaform(request.POST or None , request.FILES or None ,instance=agreg)
   if formulari.is_valid() and request.POST:
        formulari.save()
        return redirect ('index')
   return render (request,"editar.html", {'formulari': formulari})

