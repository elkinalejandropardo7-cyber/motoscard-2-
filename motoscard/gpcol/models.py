
from django.db import models


class Piloto(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, unique=True)
    tipo_de_documento = models.CharField(max_length=25)
    numero_de_competicion = models.CharField(max_length=20, unique=True)
    rh = models.CharField(max_length=5)

    carrera = models.ManyToManyField(
        'Carrera',
        related_name='pilotos',
        blank=True,
    )

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.documento}'


class Escenario(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo_de_pista = models.CharField(max_length=30)
    capacidad_de_espectadores = models.PositiveIntegerField()

    def __str__(self):
        return (
            f'{self.nombre} - {self.ciudad} - '
            f'{self.tipo_de_pista} - '
            f'{self.capacidad_de_espectadores}'
        )


class Carrera(models.Model):
    campeonato = models.CharField(max_length=30)
    nombre_valida = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    escenario = models.ForeignKey(
        Escenario,
        on_delete=models.CASCADE,
        related_name='carreras',
    )
    categoria_habilidades = models.CharField(max_length=300)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return (
            f'{self.campeonato} - {self.nombre_valida} - '
            f'{self.fecha_inicio} - {self.escenario} - '
            f'{self.categoria_habilidades} - {self.estado}'
        )
