# Generated by Django 3.2.7 on 2022-09-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0011_auto_20211012_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='motorpool/brands/'),
        ),
    ]
