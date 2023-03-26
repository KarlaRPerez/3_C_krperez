from django import forms
from .models import Usuarios

class creaform (forms.ModelForm):
    class  Meta:
        model =  Usuarios
        fields = '__all__'
        
class Usuariform (forms.ModelForm):
    class  Meta:
        model =  Usuarios
        fields = '__all__'