from django import forms
from .models import Cliente
from .models import Agenda

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        #fields = ["rut", "id_reserva", "nombres", "apellidos ", "telefono", "correo"]
        fields = '__all__'

class AgendaArriendoForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'