# Generated by Django 4.2.1 on 2023-06-02 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_alter_buyer_options_buyer_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordervehicle',
            name='vehicle',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='car_price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AddField(
            model_name='ordervehicle',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carapp.vehicle'),
        ),
    ]
