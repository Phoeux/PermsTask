# Generated by Django 3.1.7 on 2021-03-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210325_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotterpattern',
            name='stats',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]