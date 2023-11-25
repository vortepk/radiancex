# Generated by Django 4.2.7 on 2023-11-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_patient_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='treatment_regions',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('regions_supported', models.ManyToManyField(to='doctor.treatmentregion')),
            ],
        ),
    ]
