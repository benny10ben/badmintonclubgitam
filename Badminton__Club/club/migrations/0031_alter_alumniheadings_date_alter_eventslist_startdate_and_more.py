# Generated by Django 5.0.3 on 2024-03-18 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0030_alter_alumniheadings_date_alter_eventslist_startdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 7, 43, 58, 57696)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 7, 43, 58, 56071)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 7, 43, 58, 56674)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 7, 43, 58, 56442)),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2024, 3, 18, 7, 43, 58, 57162)),
        ),
    ]