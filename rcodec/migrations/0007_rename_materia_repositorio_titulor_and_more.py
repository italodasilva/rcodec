# Generated by Django 4.0.5 on 2022-11-14 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcodec', '0006_tcc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repositorio',
            old_name='materia',
            new_name='titulor',
        ),
        migrations.RenameField(
            model_name='tcc',
            old_name='descricao',
            new_name='titulot',
        ),
    ]