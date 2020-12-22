import datetime

from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TipoRoscon(CommonModel):
    tipo = models.CharField(max_length=50, unique=True)


class Roscon(CommonModel):
    cantidad = models.PositiveIntegerField()
    tipo_roscon = models.ForeignKey(
        TipoRoscon,
        on_delete=models.PROTECT
    )
    anno = models.SmallIntegerField(default=datetime.date.today().year)


class Token(CommonModel):
    token = models.CharField(max_length=60, unique=True)
