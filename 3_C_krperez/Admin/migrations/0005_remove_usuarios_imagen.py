# Generated by Django 4.0.5 on 2023-03-24 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_login_remove_usuarios_fnac_remove_usuarios_fregistro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='imagen',
        ),
    ]