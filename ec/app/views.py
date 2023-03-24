from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from . models import Producto,Customer,Carrito
from . forms import formularioregistroclientes,CustomersProfileForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView



# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contacto(request):
    return render(request,"app/contacto.html")

class CategoriaView(View):
    def get(self,request,val):
        product= Producto.objects.filter(categoria=val)
        title= Producto.objects.filter(categoria=val).values("title")
        return render(request,"app/categoria.html",locals())
    

class CategoriaTitle(View):
    def get(self,request,val):
        product= Producto.objects.filter(title=val)
        title= Producto.objects.filter(categoria=product[0].categoria).values("title")
        return render(request,"app/categoria.html",locals())


class ProductoDetalle(View):
    def get(self,request,pk):
        product= Producto.objects.get(pk=pk)
        return render(request,"app/producto_detalle.html",locals())


class formularioregistroclientesViews(View):
    def get(self,request):
        form = formularioregistroclientes()
        return render(request,"app/registrocliente.html",locals())
    def post(self,request):
        form = formularioregistroclientes(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"¡Felicidades! Registro de usuario con éxito")
        else:
            messages.warning(request,"Datos de entrada inválidos")
        return render(request,"app/registrocliente.html",locals())
    
class ProfileView(View):
    def get(self,request):
        form = CustomersProfileForm()
        return render(request,"app/perfil.html",locals())
    
    def post(self,request):
            form = CustomersProfileForm(request.POST)
            if form.is_valid():
                usuario = request.user
                nombre= form.cleaned_data['nombre']
                direccion = form.cleaned_data['direccion']
                ciudad = form.cleaned_data['ciudad']
                móvil= form.cleaned_data['móvil']
                provincia= form.cleaned_data['provincia']
                codigo_postal = form.cleaned_data['codigo_postal']

                reg = Customer(usuario=usuario, nombre=nombre,direccion=direccion, móvil=móvil, ciudad=ciudad,provincia=provincia,codigo_postal=codigo_postal)
                reg.save()
                messages.success(request,"¡Felicidades! Perfil guardado con éxito")
            else:
                messages.warning(request,"Datos de entrada inválidos")
            return render(request,"app/perfil.html",locals())

def direccion(request):
    agregar= Customer.objects.filter(usuario=request.user)
    return render(request,"app/direccion.html",locals())


class updateDireccion(View):
    def get(self,request,pk):
        agregar= Customer.objects.get(pk=pk)
        form= CustomersProfileForm(instance=agregar)
        return render(request,"app/updateDireccion.html",locals())


    def post(self,request,pk):
        form= CustomersProfileForm(request.POST)
        if form.is_valid():
            agregar= Customer.objects.get(pk=pk)
            agregar.nombre = form.cleaned_data['nombre']
            agregar.direccion = form.cleaned_data['direccion']
            agregar.ciudad = form.cleaned_data['ciudad']
            agregar.móvil = form.cleaned_data['móvil']
            agregar.provincia = form.cleaned_data['provincia']
            agregar.codigo_postal = form.cleaned_data['codigo_postal']
            agregar.save ()
            messages.success(request, "¡Felicidades! Actualización de perfil con éxito")
        else:
            messages. warning (request, "Datos de entrada no válidos")
        return redirect("adress")
    
def agregar_a_carrito(request):
    usuario=request.user
    producto_id=request.Get.get('producto_id')
    producto= Producto.objects.get(id=producto_id)
    Carrito(usuario=usuario,producto=producto).save()
    return redirect('/carrito')

def mostrar_carro(request):
    usuario=request.user
    carrito= Carrito.objects.filter(usuario=usuario)
    return render(request,'app/agregar-a-carrito.html',locals())
            