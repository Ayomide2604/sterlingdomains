# Generated by Django 4.2.7 on 2024-08-19 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0011_alter_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='photo',
        ),
    ]
