# Generated by Django 4.2.2 on 2023-07-09 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0024_remove_eventslist_enddate_alter_alumniheadings_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 31, 17, 404943)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 19, 31, 17, 403515)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 31, 17, 404030)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 31, 17, 403804)),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 31, 17, 404500)),
        ),
    ]
