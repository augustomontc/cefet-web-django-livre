# Generated by Django 2.1.3 on 2018-12-03 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pastel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farinha', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Recheio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img_recheio', models.ImageField(upload_to='imgs', verbose_name='Imagem')),
            ],
        ),
        migrations.AddField(
            model_name='pastel',
            name='recheio',
            field=models.ManyToManyField(to='app.Recheio'),
        ),
    ]
