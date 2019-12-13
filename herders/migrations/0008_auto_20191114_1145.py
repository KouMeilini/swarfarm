# Generated by Django 2.1.11 on 2019-11-14 19:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0007_remove_runecraftinstance_ancient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runeinstance',
            name='substat_craft_values',
        ),
        migrations.RemoveField(
            model_name='runeinstance',
            name='substat_crafts',
        ),
        migrations.AddField(
            model_name='runeinstance',
            name='substats_enchanted',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(default=False), default=list, size=4),
        ),
        migrations.AddField(
            model_name='runeinstance',
            name='substats_grind_value',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=list, size=4),
        ),
    ]
