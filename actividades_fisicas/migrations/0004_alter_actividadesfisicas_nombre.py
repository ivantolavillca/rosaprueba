# Generated by Django 5.1.1 on 2025-04-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades_fisicas', '0003_delete_actividades_fisicas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadesfisicas',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Realiza actividad física?'),
        ),
    ]
