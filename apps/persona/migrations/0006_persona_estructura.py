# Generated by Django 3.0.3 on 2020-02-26 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0001_initial'),
        ('persona', '0005_auto_20200226_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estructura',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estructura.Estructura'),
            preserve_default=False,
        ),
    ]
