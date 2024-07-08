from django.urls import path
from .views import tareas_pasadas_view

urlpatterns = [
    path('tareas_pasadas/', tareas_pasadas_view, name='tareas_pasadas'),
]
