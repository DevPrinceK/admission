# Generated by Django 4.0.3 on 2022-03-15 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_rename_fist_choice_bio_first_choice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=25, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('network', models.CharField(max_length=15)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('status_code', models.CharField(max_length=5)),
                ('status_message', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]