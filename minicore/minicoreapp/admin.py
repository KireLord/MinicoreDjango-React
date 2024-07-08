from django.contrib import admin
from .models import Empleado, Proyecto, Tarea

# Registrar los modelos para que aparezcan en el panel de administración
admin.site.register(Empleado)
admin.site.register(Proyecto)
admin.site.register(Tarea)
