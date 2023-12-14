# Generated by Django 4.2.7 on 2023-12-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descrip', models.CharField(max_length=100)),
                ('stock', models.IntegerField(max_length=5)),
                ('precio', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=25)),
                ('mail', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=80)),
                ('productos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoD', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoP', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
