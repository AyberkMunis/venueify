# Generated by Django 4.0.3 on 2022-07-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_place_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='base',
            field=models.CharField(default='', max_length=50),
        ),
    ]
