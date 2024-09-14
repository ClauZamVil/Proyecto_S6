from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def iniciar_sesion(request):
    usuario1 = request.POST['usuario']
    contra1 = request.POST ['contra']
    try:
        user1 = User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error (request, 'El usuario o la contraseña son incorrectas')
        return redirect('iniciar')

    pass_valida = check_password(contra1,user1.password)
    if not pass_valida:
        messages.error (request, 'El usuario o la contraseña son incorrectas')
        return redirect ('iniciar') 
    usuario2 = Usuario.objects.get(username = usuario1.contrasennia = contra1)   
    user = authenticate(username=usuario1, password=contra1)
    if user is not None:
        login(request, user)
        if (usuario2.tipousuario.idTipoUsuario == 1)
            return redirect ('menu_admin')
        else:
            contexto = {"usuario":usuario2}
            return render (request, 'Inicio/index.html', contexto)
        #A backend authenticated the credentials
    else:
        print("8")
        #No backend authenticated the credentials

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar')
        


#Templates
def index(request):
    return render(request,'core/index.html')

def CategoriaAventura(request):
    return render(request, 'core/CategoriaAventura.html')

def Aventura1(request):
    return render(request, 'core/Aventura1.html')

def Aventura2(request):
    return render(request, 'core/Aventura2.html')

def CategoriaConduccion(request):
    return render(request, 'core/CategoriaConduccion.html')

def categoriaDeportes(request):
    return render(request, 'core/categoriaDeportes.html')

def CategoriaEstrategia(request):
    return render(request, 'core/CategoriaEstrategia.html')

def CategoriaInfantiles(request):
    return render(request, 'core/CategoriaInfantiles.html')

def Conduccion1(request):
    return render(request, 'core/Conduccion1.html')

def Conduccion2(request):
    return render(request, 'core/Conduccion2.html')

def Deporte1(request):
    return render(request, 'core/Deporte1.html')

def Deporte2(request):
    return render(request, 'core/Deporte2.html')

def Estrategia1(request):
    return render(request, 'core/Estrategia1.html')

def Estrategia2(request):
    return render(request, 'core/Estrategia2.html')

def Infantil1(request):
    return render(request, 'core/Infantil1.html')

def Infantil2(request):
    return render(request, 'core/Infantil2.html')

def login(request):
    return render(request, 'core/login.html')

def Principal(request):
    return render(request, 'core/Principal.html')

def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')

def register(request):
    return render(request, 'core/register.html')

def home (request):
    #accediendo al objeto que contiene los datos de la base
    #el metodo all traera todos los vehiculos que estan en la table
    vehiculos= Vehiculo.objects.all()
    #ahora crearemos una variable que le pase los datos del vihiculo al template
    datos = {
        'vehiculos': vehiculos
    }
    # ahora le agregamos para que se envie al template
    return render (request, 'core/home.html', datos)

def form_vehiculo(request):
    return render (request, 'core/form_vehiculo.html')

def form_vehiculo(request):
    datos = {
        'form': VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render (request, 'core/form_vehiculo.html',datos)     

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }   

    return render(request, 'core/form_mod_vehiculo.html',datos)

def form_del_vehiculo(request, id):
    #el id es el identificador de la tabla de Vehiculos
    #buscando los datos en la base de datos

    vehiculo = Vehiculo.objects.get(patente=id)
    #eliminamos el vehiculo de la patente buscada
    vehiculo.delete()
    #ahora redirigimos a la pagina home con el listado
    return redirect(to="home")
            