# Generated by Django 4.2.6 on 2023-10-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0005_employee_alter_domain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
