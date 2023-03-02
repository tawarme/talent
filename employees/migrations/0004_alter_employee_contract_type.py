# Generated by Django 4.1.7 on 2023-03-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contract_type',
            field=models.CharField(choices=[('CONT', 'Contractor'), ('PLAN', 'Planilla')], max_length=20),
        ),
    ]