# Generated by Django 4.0.5 on 2023-03-23 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_alter_usuarios_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='f_nac',
            new_name='fnac',
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='f_registro',
            new_name='fregistro',
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='usuarios',
        ),
    ]