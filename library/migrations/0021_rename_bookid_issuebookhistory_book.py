# Generated by Django 4.0.1 on 2022-03-15 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_alter_reservedbooks_datereserved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebookhistory',
            old_name='bookid',
            new_name='book',
        ),
    ]
