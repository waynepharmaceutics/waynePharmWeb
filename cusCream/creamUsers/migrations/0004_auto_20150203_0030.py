# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creamUsers', '0003_auto_20150203_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingrediant1',
            field=models.ForeignKey(related_name='ingredient_cream', to='creamUsers.Ingredient'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='ingrediant2',
            field=models.ForeignKey(related_name='ingredient_penetrate', to='creamUsers.Ingredient'),
            preserve_default=True,
        ),
    ]
