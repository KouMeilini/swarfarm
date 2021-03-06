# Generated by Django 2.1.7 on 2019-07-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0015_auto_20190615_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='natural_stars',
            field=models.IntegerField(choices=[(1, '1<span class="glyphicon glyphicon-star"></span>'), (2, '2<span class="glyphicon glyphicon-star"></span>'), (3, '3<span class="glyphicon glyphicon-star"></span>'), (4, '4<span class="glyphicon glyphicon-star"></span>'), (5, '5<span class="glyphicon glyphicon-star"></span>'), (6, '6<span class="glyphicon glyphicon-star"></span>')], default=1, help_text="Stars of the monster's lowest awakened form"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monster',
            name='base_stars',
            field=models.IntegerField(choices=[(1, '1<span class="glyphicon glyphicon-star"></span>'), (2, '2<span class="glyphicon glyphicon-star"></span>'), (3, '3<span class="glyphicon glyphicon-star"></span>'), (4, '4<span class="glyphicon glyphicon-star"></span>'), (5, '5<span class="glyphicon glyphicon-star"></span>'), (6, '6<span class="glyphicon glyphicon-star"></span>')], help_text='Display stars in game'),
        ),
    ]
