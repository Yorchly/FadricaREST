import uuid

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from api.models import Token


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("CREANDO TOKEN"))
        db_uuid = str(uuid.uuid4())
        try:
            Token.objects.create(token=db_uuid)
        except IntegrityError:
            raise CommandError("¡ERROR! Token repetido, ejecute de nuevo el comando.")

        self.stdout.write(self.style.SUCCESS("TOKEN CREADO CON ÉXITO: {}".format(db_uuid)))
