# Generated by Django 2.2 on 2020-12-21 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201221_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roscon',
            name='tipo_roscon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.TipoRoscon'),
        ),
        migrations.AlterField(
            model_name='tiporoscon',
            name='tipo',
            field=models.CharField(max_length=50),
        ),
    ]
