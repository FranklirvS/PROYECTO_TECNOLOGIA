from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATE_CHOICES = (
    ('AZU', 'Azuay'),
    ('BOL', 'Bolívar'),
    ('CAN', 'Cañar'),
    ('CAR', 'Carchi'),
    ('CHI', 'Chimborazo'),
    ('COT', 'Cotopaxi'),
    ('EOR', 'El Oro'),
    ('ESM', 'Esmeraldas'),
    ('GAL', 'Galápagos'),
    ('GUA', 'Guayas'),
    ('IMB', 'Imbabura'),
    ('LOJ', 'Loja'),
    ('LRO', 'Los Ríos'),
    ('MAN', 'Manabí'),
    ('MSA', 'Morona Santiago'),
    ('NAP', 'Napo'),
    ('ORE', 'Orellana'),
    ('PAS', 'Pastaza'),
    ('PIC', 'Pichincha'),
    ('SUC', 'Sucumbíos'),
    ('TUN', 'Tungurahua'),
    ('ZCH', 'Zamora Chinchipe'),
)




CATEGORY_CHOICES=(
    ('tl','Telefono'),
    ('tb','Tablet'),
    ('lp','Laptop'),
    ('ac','Accesorios'),
    ('md','Mando'),
    ('cs','Consola'),
)




class Producto(models.Model):
    title=models.CharField(max_length=100)
    precio_venta=models.FloatField()
    precio_descontado=models.FloatField()
    descripcion=models.TextField()
    composicion=models.TextField(default='')
    prodapp=models.TextField(default='')
    categoria=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    producto_imagen= models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    nombre= models.CharField (max_length=200)
    direccion = models.CharField (max_length=200)
    ciudad = models.CharField (max_length=50)
    móvil = models.IntegerField (default=0)
    codigo_postal= models.IntegerField ()
    provincia = models.CharField(choices=STATE_CHOICES, max_length=100)
    def _str_(self) :
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad= models.PositiveIntegerField(default=-1)

    @property
    def total_costo(self):
        return self.cantidad * self.producto.precio_descontado