# Generated by Django 3.0.3 on 2020-02-26 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipio', '0001_initial'),
        ('organismo', '0001_initial'),
        ('sector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoPaterno', models.CharField(max_length=100)),
                ('apellidoMaterno', models.CharField(max_length=100)),
                ('sexo', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], default=1)),
                ('fechaNacimiento', models.DateField()),
                ('clave_electoral', models.CharField(default=0, max_length=30)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('calle_numero', models.CharField(max_length=100, null=True)),
                ('correo', models.EmailField(max_length=100)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('whatsapp', models.CharField(max_length=100, null=True)),
                ('nivel_confianza', models.IntegerField(default=0)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipio.Municipio')),
                ('organismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organismo.Organismo')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sector.Sector')),
            ],
        ),
    ]
