# Generated by Django 4.1 on 2022-09-05 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10)),
                ('observaciones', models.TextField()),
                ('habilitado', models.BooleanField()),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'Movil',
                'verbose_name_plural': 'Moviles',
            },
        ),
    ]
