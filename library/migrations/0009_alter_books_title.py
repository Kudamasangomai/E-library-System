# Generated by Django 3.2.9 on 2021-12-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_books_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=101),
        ),
    ]
