# Generated by Django 4.2.7 on 2023-12-16 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_entry_record_security_note_delete_amer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='security_note',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
