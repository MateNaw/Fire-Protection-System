# Generated by Django 3.1.3 on 2020-12-06 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20201206_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='localization',
            new_name='location',
        ),
    ]
