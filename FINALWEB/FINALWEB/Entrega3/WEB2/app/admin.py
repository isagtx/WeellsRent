from django.contrib import admin
from .models import Cliente, Vehiculo, Reserva, Empleado, Agenda
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Reserva)
admin.site.register(Empleado)
admin.site.register(Agenda)