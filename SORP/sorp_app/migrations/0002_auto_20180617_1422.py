# Generated by Django 2.0.6 on 2018-06-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='year',
            field=models.IntegerField(default=2018),
        ),
    ]
