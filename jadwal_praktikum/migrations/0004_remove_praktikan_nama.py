# Generated by Django 4.1 on 2023-08-16 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal_praktikum', '0003_remove_asprak_kelas_jadwal_kelas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='praktikan',
            name='nama',
        ),
    ]
