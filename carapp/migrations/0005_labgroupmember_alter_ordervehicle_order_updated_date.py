# Generated by Django 4.2.1 on 2023-06-14 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_description_alter_ordervehicle_order_updated_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabGroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('personal_page', models.URLField()),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.AlterField(
            model_name='ordervehicle',
            name='order_updated_date',
            field=models.DateField(default=datetime.date(2023, 6, 14)),
        ),
    ]
