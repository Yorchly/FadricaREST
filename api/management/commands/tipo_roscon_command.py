from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from api.models import TipoRoscon


TIPO_ROSCON = (
    "Nata",
    "Crema",
    "Cidra",
    "Trufa",
    "Seco",
    "Especial"
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("CARGANDO TIPO DE ROSCONES EN LA BASE DE DATOS"))
        try:
            TipoRoscon.objects.bulk_create([TipoRoscon(tipo=tipo_roscon) for tipo_roscon in TIPO_ROSCON])
        except IntegrityError:
            raise CommandError("¡ERROR! Los Tipo de Roscon ya se encuentran creados")

        self.stdout.write(self.style.SUCCESS("¡TIPOS DE ROSCÓN CARGADOS!"))

