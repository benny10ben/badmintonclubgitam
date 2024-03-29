# Generated by Django 4.2.2 on 2023-07-03 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_eventslist_register_soon_alter_eventslist_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventslist',
            name='EndDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 3, 19, 12, 784189)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='Register_Soon',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 3, 19, 12, 784173)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 3, 19, 12, 784682)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 3, 19, 12, 784466)),
        ),
    ]
