# Generated by Django 4.2.7 on 2024-08-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='offer',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='domain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='domain_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
