# Generated by Django 2.2 on 2020-12-21 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_roscon_año'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roscon',
            old_name='año',
            new_name='anno',
        ),
    ]
