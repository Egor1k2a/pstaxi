# Generated by Django 3.2.7 on 2021-10-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0007_alter_auto_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=210),
        ),
    ]