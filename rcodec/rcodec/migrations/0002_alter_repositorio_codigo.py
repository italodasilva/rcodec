# Generated by Django 4.0.5 on 2022-10-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcodec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorio',
            name='codigo',
            field=models.DecimalField(decimal_places=1, max_digits=5, primary_key=True, serialize=False),
        ),
    ]