# Generated by Django 3.0.3 on 2020-02-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='nivel_confianza',
            field=models.IntegerField(default=0),
        ),
    ]
