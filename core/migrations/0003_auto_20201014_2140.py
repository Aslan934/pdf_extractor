# Generated by Django 3.1.1 on 2020-10-14 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_file_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='user',
            new_name='owner',
        ),
    ]
