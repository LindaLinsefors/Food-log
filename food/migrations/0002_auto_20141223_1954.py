# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodentry',
            old_name='description',
            new_name='ingredients',
        ),
        migrations.AddField(
            model_name='foodentry',
            name='food_stuff',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='ingredients',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
