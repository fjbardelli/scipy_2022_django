# Generated by Django 4.1.1 on 2022-09-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_alter_registro_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
