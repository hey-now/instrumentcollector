# Generated by Django 4.1.3 on 2022-11-16 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_accessory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accessory',
            new_name='Played',
        ),
    ]