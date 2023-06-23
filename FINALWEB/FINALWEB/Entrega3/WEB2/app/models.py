from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=10)
    id_reserva = models.CharField(max_length=6,null=True)
    nombres_cli = models.CharField(max_length=30)
    apellidos_cli = models.CharField(max_length=30)
    telefono_cli = models.CharField(max_length=30)
    correo_cli = models.EmailField(null=True)
    def __str__(self):
        return self.rut_cliente
    
class Vehiculo(models.Model):
    id_vehiculo = models.CharField(max_length=4)
    id_reserva = models.CharField(max_length=6, null=True)
    patente_veh = models.CharField(max_length=6)
    color_veh = models.CharField(max_length=10)
    modelo_veh = models.CharField(max_length=12)
    def __str__(self):
        return self.id_vehiculo

class Reserva(models.Model):
    id_reserva = models.CharField(max_length=6)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    fecha = models.DateTimeField(null=False, blank=False)
    fecha_entrega = models.DateTimeField(null=False, blank=False)
    def __str__(self):
        return self.id_reserva

class Empleado(models.Model):
    rut_emp = models.CharField(max_length=10)
    nombres_emp = models.CharField(max_length=30)
    apellidos_emp = models.CharField(max_length=30)
    direccion_emp = models.CharField(max_length=30)
    sueldo_emp = models.CharField(max_length=7)
    id_reserva = models.CharField(max_length=6, null=True)
    def __str__(self):
        return self.rut_emp
    
opciones_arriendo = [
    [0, "Empresa ($100.000)"],
    [1, "Normal ($130.000)"]
]

opciones_veh = [
    [0, "Camioneta"],
    [1, "Camión"],
    [2, "Auto"],
    [3, "Suv"]
]

class Agenda(models.Model):
    nombrecompleto = models.CharField(max_length=60)
    correo = models.EmailField()
    tipoarriendo = models.IntegerField(choices=opciones_arriendo)
    tipoveh = models.IntegerField(choices=opciones_veh)
    
    def __str__(self):
        return self.nombrecompleto