from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import get_current_year


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
    anno = models.SmallIntegerField(default=get_current_year())


class Token(CommonModel):
    token = models.CharField(max_length=60)
