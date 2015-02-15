# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creamUsers', '0004_auto_20150203_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ingrediant1',
            new_name='ingredient1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ingrediant2',
            new_name='ingredient2',
        ),
    ]
