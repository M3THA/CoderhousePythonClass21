from socket import fromshare
from sqlite3 import IntegrityError
from django import forms

class CursoFormulario(forms.Form):
    curso=forms.CharField()
    comision= forms.IntegerField()


class ProfeFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)
