# Generated by Django 3.2.6 on 2021-08-15 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudio', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('documento', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('url_file', models.FileField(upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('estudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio.estudiomodel')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.docidentidadmodel')),
            ],
        ),
    ]
