# Generated by Django 3.0.3 on 2020-02-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0011_auto_20200226_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
