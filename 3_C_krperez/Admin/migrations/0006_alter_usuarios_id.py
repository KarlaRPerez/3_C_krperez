# Generated by Django 4.0.5 on 2023-03-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_remove_usuarios_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
