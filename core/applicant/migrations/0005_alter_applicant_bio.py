# Generated by Django 4.0.3 on 2022-03-15 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0004_alter_transaction_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='bio',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='applicant.bio'),
        ),
    ]
