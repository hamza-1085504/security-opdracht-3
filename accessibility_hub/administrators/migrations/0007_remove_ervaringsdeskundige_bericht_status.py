# Generated by Django 5.0.2 on 2024-03-09 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0006_remove_onderzoek_organisatie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ervaringsdeskundige',
            name='bericht_status',
        ),
    ]
