# Generated by Django 4.0.1 on 2022-03-10 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_reservedbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedbooks',
            name='datereserved',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
