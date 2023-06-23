from django.shortcuts import render
from .forms import RegistroForm
from .forms import AgendaArriendoForm
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def agenda(request):
    data = {
        'form1': AgendaArriendoForm()
    }
    if request.method == 'POST':
        formulario = AgendaArriendoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agendado!"
        else:
            data ["form1"] = formulario
    return render(request, 'app/agenda.html', data)

def registro(request):
    data = {
        'form': RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Usuario registrado!"
        else:
            data ["form"] = formulario
            
    return render(request, 'app/registro.html', data)