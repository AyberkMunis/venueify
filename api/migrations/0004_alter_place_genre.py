# Generated by Django 4.0.3 on 2022-07-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_place_genre_alter_place_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='genre',
            field=models.CharField(default='', max_length=50),
        ),
    ]
