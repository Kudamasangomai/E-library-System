# Generated by Django 3.2.9 on 2021-12-22 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_issuedbooks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbooks',
            old_name='userdid',
            new_name='userid',
        ),
    ]
