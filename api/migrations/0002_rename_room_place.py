# Generated by Django 4.0.3 on 2022-07-03 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Place',
        ),
    ]