from rest_framework import serializers

class TareaPasadaSerializer(serializers.Serializer):
    tarea = serializers.CharField()
    empleado = serializers.CharField()
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()
    dias_pasados = serializers.IntegerField()
    proyecto = serializers.CharField()
