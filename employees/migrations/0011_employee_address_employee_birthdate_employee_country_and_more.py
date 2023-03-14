# Generated by Django 4.1.7 on 2023-03-14 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_param_paramitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='birthdate',
            field=models.DateField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.ForeignKey(limit_choices_to={'param__name': 'country'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_id', to='employees.paramitem'),
        ),
        migrations.AddField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='nationality',
            field=models.ForeignKey(limit_choices_to={'param__name': 'nationality'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nationality_id', to='employees.paramitem'),
        ),
        migrations.AddField(
            model_name='employee',
            name='nickname',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='second_last_name',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
