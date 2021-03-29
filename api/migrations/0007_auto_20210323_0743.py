# Generated by Django 3.1.7 on 2021-03-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210322_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plotterpattern',
            old_name='pattern_id',
            new_name='pattern',
        ),
        migrations.RenameField(
            model_name='plotterpattern',
            old_name='plotter_id',
            new_name='plotter',
        ),
        migrations.AlterField(
            model_name='plotterpattern',
            name='stats',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
