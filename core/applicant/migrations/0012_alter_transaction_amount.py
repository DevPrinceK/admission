# Generated by Django 4.0.3 on 2022-03-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0011_remove_program_program_id_program_program_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
