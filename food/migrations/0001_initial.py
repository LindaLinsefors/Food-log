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
                ('date', models.DateTimeField()),
                ('amount_text', models.CharField(max_length=20)),
                ('amount_value', models.FloatField(validators=food.models.validate_poss)),
                ('description', models.CharField(max_length=500)),
                ('fruit', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('dairy', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('water', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('junk', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('veg', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('protein', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('startch', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('unknown', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('fruit', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('dairy', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('water', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('junk', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('veg', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('protein', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('startch', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
                ('unknown', models.SmallIntegerField(validators=[food.models.validate_non_neg])),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
