from django.contrib import admin

from .models import Usuarios
from .models import Login
from .models import Imagen
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Login)
admin.site.register(Imagen)
