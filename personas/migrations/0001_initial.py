# Generated by Django 5.1.1 on 2025-01-06 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clasificacion_peso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estatura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imc', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('clasificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clasificacion_peso.clasificacion')),
            ],
        ),
    ]
