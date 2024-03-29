# Generated by Django 4.2.2 on 2023-08-08 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0025_alter_alumniheadings_date_alter_eventslist_startdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventslist',
            name='Description2',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='alumniheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 3, 57, 34, 765317)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 8, 3, 57, 34, 763883)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 3, 57, 34, 764437)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 3, 57, 34, 764203)),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 3, 57, 34, 764877)),
        ),
    ]
