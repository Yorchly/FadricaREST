from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TipoRoscon(CommonModel):
    NATA = "NATA"
    TRUFA = "TRUFA"
    CREMA = "CREMA"
    CIDRA = "CIDRA"
    SECO = "SECO"
    ESPECIAL = "ESPECIAL"
    TIPO_ROSCON = [
        (NATA, "nata"),
        (TRUFA, "trufa"),
        (CREMA, "crema"),
        (CIDRA, "cidra"),
        (SECO, "seco"),
        (ESPECIAL, "especial"),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_ROSCON)


class Roscon(CommonModel):
    cantidad = models.PositiveIntegerField()
    tipo_roscon = models.OneToOneField(
        TipoRoscon,
        on_delete=models.PROTECT
    )


class Token(CommonModel):
    token = models.CharField(max_length=60)
