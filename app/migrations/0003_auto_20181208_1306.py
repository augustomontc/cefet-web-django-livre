# Generated by Django 2.1.3 on 2018-12-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181206_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recheio',
            name='nome',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]
