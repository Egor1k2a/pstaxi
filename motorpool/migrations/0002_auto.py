# Generated by Django 3.2.7 on 2021-09-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('auto_class', models.CharField(choices=[('e', 'economy'), ('c', 'comfort'), ('b', 'business')], default='e', max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
