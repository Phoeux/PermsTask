# Generated by Django 3.1.7 on 2021-03-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210325_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='printed_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
