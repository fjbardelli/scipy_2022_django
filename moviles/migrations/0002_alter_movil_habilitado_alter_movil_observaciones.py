# Generated by Django 4.1 on 2022-09-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movil',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='movil',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]