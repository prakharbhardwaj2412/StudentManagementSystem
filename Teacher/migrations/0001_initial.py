# Generated by Django 2.2 on 2020-07-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEACHER_USERNAME', models.CharField(max_length=250)),
                ('PASSWORD', models.CharField(max_length=250)),
            ],
        ),
    ]
