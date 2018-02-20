# Generated by Django 2.0.2 on 2018-02-19 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
        ('league', '0001_initial'),
        ('player', '0002_auto_20180219_0750'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('person', 'league')},
        ),
        migrations.AlterUniqueTogether(
            name='playerhandicap',
            unique_together={('player', 'week')},
        ),
        migrations.AlterUniqueTogether(
            name='playerround',
            unique_together={('player', 'week')},
        ),
    ]
