# Generated by Django 5.0.1 on 2024-02-27 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_vragen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vragen',
            old_name='vraag',
            new_name='vraagtitel',
        ),
    ]
