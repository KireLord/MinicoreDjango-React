from django.db import models

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de ID explícito
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    proyectos = models.ManyToManyField('Proyecto')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de ID explícito
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de ID explícito
    descripcion = models.CharField(max_length=255)
    fecha_empezar = models.DateField()
    trabajo_estimado = models.IntegerField()
    estado_choices = [
        ('In progress', 'In progress'),
        ('Done', 'Done')
    ]
    estado = models.CharField(max_length=20, choices=estado_choices)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
