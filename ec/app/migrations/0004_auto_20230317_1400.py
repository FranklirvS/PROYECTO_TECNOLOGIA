# Generated by Django 3.0 on 2023-03-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='zipcode',
            new_name='codigo_postal',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='localidad',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='estado',
            new_name='provincia',
        ),
    ]
