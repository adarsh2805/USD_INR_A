# Generated by Django 3.0.5 on 2023-03-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GSDAPP', '0002_auto_20230327_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='INR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rupee', models.IntegerField()),
            ],
        ),
    ]
