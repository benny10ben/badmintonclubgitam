# Generated by Django 4.2.2 on 2023-07-09 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0022_alumnimembers_quote_teammembers_quote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 7, 28, 959664)),
        ),
        migrations.AlterField(
            model_name='alumnimembers',
            name='Quote',
            field=models.TextField(blank=True, default='...', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='EndDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 19, 7, 28, 958289)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 19, 7, 28, 958273)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 7, 28, 958802)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 7, 28, 958580)),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 19, 7, 28, 959234)),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='Quote',
            field=models.TextField(blank=True, default='...', max_length=100),
        ),
    ]