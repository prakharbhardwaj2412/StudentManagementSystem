# Generated by Django 2.2 on 2020-07-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Query', '0002_auto_20200718_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query_table',
            name='TIME',
        ),
        migrations.AlterField(
            model_name='query_table',
            name='STATUS',
            field=models.CharField(default='pending', max_length=25),
        ),
    ]