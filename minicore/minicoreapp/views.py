from django.utils.dateparse import parse_date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Empleado, Proyecto, Tarea
from .serializers import TareaPasadaSerializer
from datetime import datetime, timedelta

@api_view(['GET'])
def tareas_pasadas_view(request):
    fecha_ini_str = request.query_params.get('fecha_ini')
    fecha_fin_str = request.query_params.get('fecha_fin')

    if not fecha_ini_str or not fecha_fin_str:
        return Response({"error": "Faltan parámetros de fecha"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        fecha_ini = parse_date(fecha_ini_str)
        fecha_fin = parse_date(fecha_fin_str)
    except ValueError:
        return Response({"error": "Formato de fecha inválido"}, status=status.HTTP_400_BAD_REQUEST)

    print(f"Rango de fechas: {fecha_ini} a {fecha_fin}")

    tareas = Tarea.objects.filter(estado='In progress', fecha_empezar__range=(fecha_ini, fecha_fin))
    print(f"Tareas filtradas: {tareas.count()}")

    resultados = []

    for tarea in tareas:
        fecha_estimada_fin = tarea.fecha_empezar + timedelta(days=tarea.trabajo_estimado)
        dias_pasados = (datetime.now().date() - fecha_estimada_fin).days
        print(f"Tarea: {tarea.descripcion}, Fecha Estimada Fin: {fecha_estimada_fin}, Días Pasados: {dias_pasados}")
        if dias_pasados > 0:
            resultados.append({
                'tarea': tarea.descripcion,
                'empleado': f"{tarea.empleado.nombre} {tarea.empleado.apellido}",
                'fecha_inicio': tarea.fecha_empezar,
                'fecha_fin': fecha_estimada_fin,
                'dias_pasados': dias_pasados,
                'proyecto': tarea.proyecto.nombre,
            })
    
    print(f"Resultados: {resultados}")

    serializer = TareaPasadaSerializer(resultados, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)