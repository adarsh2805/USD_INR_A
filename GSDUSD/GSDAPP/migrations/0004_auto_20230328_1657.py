# Generated by Django 3.0.5 on 2023-03-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GSDAPP', '0003_inr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsdmodel',
            name='Characteristic',
            field=models.IntegerField(unique=True),
        ),
    ]
