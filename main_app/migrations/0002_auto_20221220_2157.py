# Generated by Django 2.2.12 on 2022-12-20 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='genra',
            new_name='genre',
        ),
    ]
