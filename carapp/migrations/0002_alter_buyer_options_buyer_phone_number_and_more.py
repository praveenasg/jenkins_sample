# Generated by Django 4.2.1 on 2023-06-02 22:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'verbose_name': 'Buyer'},
        ),
        migrations.AddField(
            model_name='buyer',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='area',
            field=models.CharField(choices=[('W', 'Windsor'), ('LS', 'LaSalle'), ('A', 'Amherstburg'), ('L', 'Lakeshore'), ('LE', 'Leamington'), ('CH', 'Chatham')], default='CH', max_length=2),
        ),
        migrations.CreateModel(
            name='OrderVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_vehicles_ordered', models.PositiveIntegerField(default=0)),
                ('order_status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Placed'), (2, 'Shipped'), (3, 'Delivered')], default=1)),
                ('order_updated_date', models.DateField(default=datetime.date(2023, 6, 2))),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carapp.buyer')),
                ('vehicle', models.ManyToManyField(to='carapp.vehicle')),
            ],
        ),
    ]
