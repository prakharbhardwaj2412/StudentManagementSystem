# Generated by Django 2.2 on 2020-07-16 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_student_table_ststus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_table',
            name='EMAIL',
            field=models.CharField(max_length=250),
        ),
    ]