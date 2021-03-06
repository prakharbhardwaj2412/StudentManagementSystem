# Generated by Django 2.2 on 2020-07-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=250)),
                ('LAST_NAME', models.CharField(max_length=250)),
                ('USERNAME', models.CharField(max_length=250, unique=True)),
                ('EMAIL', models.EmailField(max_length=250)),
                ('CONTACT', models.CharField(max_length=250)),
                ('BRANCH', models.CharField(max_length=250)),
                ('YEAR', models.CharField(max_length=250)),
                ('PASSWORD', models.CharField(default='STUDENT', max_length=250)),
            ],
        ),
    ]
