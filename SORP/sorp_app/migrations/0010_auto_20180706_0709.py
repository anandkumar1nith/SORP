# Generated by Django 2.0.5 on 2018-07-06 07:09

from django.db import migrations, models
import sorp_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0009_auto_20180704_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmedicalinfo',
            name='student',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='institute',
            field=models.CharField(choices=[('NIT Hamirpur', 'NIT Hamirpur'), ('IIIT Una', 'IIIT Una')], default='NIT Hamirpur', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjects',
            name='year_onwards',
            field=models.SmallIntegerField(default=2018),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='year_of_admission',
            field=models.SmallIntegerField(default=sorp_app.models.currYear),
        ),
        migrations.AlterField(
            model_name='ugbranch',
            name='id',
            field=models.SmallIntegerField(unique=True),
        ),
        migrations.DeleteModel(
            name='StudentMedicalInfo',
        ),
    ]