# Generated by Django 4.0.3 on 2022-07-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_alter_spotifytoken_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste', models.CharField(max_length=500, unique=True)),
            ],
        ),
    ]
