# Generated by Django 2.2 on 2020-07-17 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20200716_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_table',
            old_name='STSTUS',
            new_name='STATUS',
        ),
    ]
