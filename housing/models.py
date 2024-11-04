from django.db import models

# Create your models here.
# Modelo para las Comunidades
class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para los Representantes de Familia
class RepresentanteFamilia(models.Model):
    nombre = models.CharField(max_length=100)
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE, related_name='representantes')

    def __str__(self):
        return self.nombre

# Modelo para los Progresos de Vivienda
class ProgresoVivienda(models.Model):
    PROGRESO_CHOICES = [
        (0, '0%'),
        (50, '50%'),
        (100, '100%'),
    ]

    representante = models.ForeignKey(RepresentanteFamilia, on_delete=models.CASCADE, related_name='progresos')
    fecha_registro = models.DateField(verbose_name='Fecha de Registro')

    estufa_mejorada = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Estufa mejorada')
    agua_potable = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Agua potable')
    divisiones = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Divisiones de suelo')
    piso = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Piso')
    limpieza = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Limpieza de casa')
    muebles = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Ropa ordenada en muebles')
    comida_protegida = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Comida protegida')
    
    plagas = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Sistema de trojas')
    jaulas = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Animales protegidos en jaulas')
    desparacitacion = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Vacunación y desparasitación')
    ahorro = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Plan de ahorro')
    piscicultura = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Piscicultura')
    tuberculos = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Tubérculos')
    arboles_frutales = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Arboles frutales')
    cerco_vivo = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Cerco vivo')

    reciclaje = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Botes de basura')
    banio_diario = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Baño diario')
    lavar_manos = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Lavarse las manos')
    letrina = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Letrina')
    sumidero = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Sumidero')
    escuela = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Asistencia a escuela')
    capacitaciones = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Capacitaciones comunitarias')
    vacunacion = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Plan de vacunación')
    peso = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Monitoreo de peso y salud')
    chequeo_embarazo = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Chequeos pre y post natales')
    emergencia_embarazo = models.IntegerField(choices=PROGRESO_CHOICES, default=0, verbose_name='Plan de emergencia embarazo')

    # Nuevo campo para almacenar el promedio
    promedio_progreso = models.FloatField(default=0, verbose_name='Promedio de progreso')

    def save(self, *args, **kwargs):
        # Calcular el promedio
        total_progreso = self.estufa_mejorada + self.agua_potable + self.divisiones + self.piso + self.muebles + self.limpieza + self.comida_protegida #7
        + self.plagas + self.ahorro + self.piscicultura + self.tuberculos + self.arboles_frutales + self.cerco_vivo + self.reciclaje + self.banio_diario #8
        + self.lavar_manos + self.letrina + self.sumidero + self.escuela + self.capacitaciones + self.vacunacion + self.peso + self.chequeo_embarazo + self.emergencia_embarazo #9
        self.promedio_progreso = round(total_progreso / 24, 2)
        # Llamar al método save original
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.representante.nombre} - {self.fecha_registro}'