# Generated by Django 4.2.3 on 2024-10-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC', '0009_profesional'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='TD_profesional',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('TI', 'Tarjeta de Identidad'), ('RC', 'Registro Civil'), ('PA', 'Pasaporte')], default='', max_length=2),
        ),
    ]
