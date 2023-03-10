# Generated by Django 4.1.7 on 2023-02-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=8)),
                ('area', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
                ('salary', models.IntegerField()),
                ('contract_type', models.CharField(max_length=20)),
                ('full_time', models.BooleanField()),
            ],
        ),
    ]
