# Generated by Django 3.2.7 on 2021-09-15 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0002_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='motorpool.brand'),
        ),
    ]
