# Generated by Django 3.1.7 on 2021-03-26 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_pattern_printed_num'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plotterpattern',
            unique_together={('plotter', 'pattern')},
        ),
    ]