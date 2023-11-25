# Generated by Django 4.2.7 on 2023-11-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=1024)),
                ('slots', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('family', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('family', models.CharField(max_length=1024)),
                ('weight', models.IntegerField()),
                ('fractions_number', models.IntegerField()),
                ('gender', models.CharField(max_length=1024)),
                ('condition', models.CharField(max_length=1024)),
                ('email', models.CharField(max_length=1024)),
                ('treat_date', models.ManyToManyField(to='doctor.calendar')),
            ],
        ),
    ]
