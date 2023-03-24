from django.contrib import admin
from . models import Producto, Customer, Carrito

# Register your models here.
@admin.register(Producto)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display =['id','title','precio_descontado','categoria','producto_imagen']

@admin.register(Customer)
class CustomerModelAdmin (admin.ModelAdmin):
    list_display=['id', 'usuario', 'direccion', 'ciudad','móvil', 'provincia', 'codigo_postal']

@admin.register(Carrito)
class CarritoModelAdmin(admin.ModelAdmin):
    list_display=['id','usuario','producto','cantidad']