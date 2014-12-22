# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import food.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.CharField(max_length=30)),
                ('quantity', models.FloatField(validators=food.models.validate_poss)),
                ('description', models.CharField(max_length=500)),
                ('fruit', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('dairy', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('water', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('junk', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('veg', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('protein', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('startch', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('unknown', models.SmallIntegerField(validators=[food.models.validate_percent])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('fruit', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('dairy', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('water', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('junk', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('veg', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('protein', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('startch', models.SmallIntegerField(validators=[food.models.validate_percent])),
                ('unknown', models.SmallIntegerField(validators=[food.models.validate_percent])),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
