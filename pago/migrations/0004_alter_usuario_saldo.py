# Generated by Django 5.1.1 on 2024-09-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0003_alter_usuario_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='saldo',
            field=models.FloatField(default=0),
        ),
    ]
