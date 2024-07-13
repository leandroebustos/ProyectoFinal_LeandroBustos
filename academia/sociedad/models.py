from django.db import models

# Modelo de la aplicación
class Piloto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auto_modelo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Piloto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Estadisticas(models.Model):
    auto_modelo = models.ForeignKey(Auto_modelo, on_delete=models.CASCADE)
    año = models.IntegerField()
    caballos_de_fuerza = models.IntegerField()
    velocidad_maxima = models.FloatField()

    def __str__(self):
        return f"{self.auto_modelo.nombre} - {self.año}"

class Resultado(models.Model):
    auto_modelo = models.ForeignKey(Auto_modelo, on_delete=models.CASCADE)
    carrera_datos = models.DateField()
    posicion = models.IntegerField()
    mejor_vuelta = models.DurationField()

    def __str__(self):
        return f"{self.auto_modelo.nombre} - {self.carrera_dato} - Pos: {self.posicion}"