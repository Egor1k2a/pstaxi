# Generated by Django 3.2.7 on 2021-09-15 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0004_auto_20210915_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiclePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=30, verbose_name='Идентификаторный номер (VIN)')),
                ('engine_volume', models.SmallIntegerField(verbose_name='Объём двигателя, куб.см')),
                ('engine_power', models.SmallIntegerField(verbose_name='Мощность двигателя, л.с.')),
                ('auto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motorpool.auto')),
            ],
            options={
                'verbose_name': 'Паспорт машины',
                'verbose_name_plural': 'Паспорта машин',
            },
        ),
    ]
