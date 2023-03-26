from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null=False)
    apellido = models.CharField(max_length=30,null=False)
    genero = models.CharField(max_length=50, null=False)
    telefono = models.IntegerField(null=False)
    class Meta:
        db_table = 'usuarios'


class Login (models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=100)
    password= models.CharField(max_length=50)
    nombre =models.CharField(max_length=50)
    tipousu =models.IntegerField()

class Imagen (models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=100,verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    descripcion =models.TextField(verbose_name="Descripcion",null=True)
    
    def delete (self, using=None , keep_parents=False ):
         self.imagen.storage.delete(self.imagen.name)
         super().delete()
         
         
class Registro (models.Model):
    id = models.AutoField(primary_key=True)
    usuario1=models.CharField(max_length=100)
    password1= models.CharField(max_length=50)
    repepaswor=models.CharField(Login,max_length=50)
   