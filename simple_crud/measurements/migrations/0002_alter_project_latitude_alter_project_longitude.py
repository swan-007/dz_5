# Generated by Django 4.1.7 on 2023-04-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
