# Generated by Django 3.1.4 on 2021-01-03 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210103_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='county',
            new_name='default_county',
        ),
    ]
