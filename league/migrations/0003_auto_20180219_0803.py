# Generated by Django 2.0.2 on 2018-02-19 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20180219_0801'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hole',
            unique_together={('nine', 'course_number'), ('nine', 'handicap'), ('nine', 'nine_number')},
        ),
    ]
