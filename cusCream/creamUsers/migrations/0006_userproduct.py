# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creamUsers', '0005_auto_20150203_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userproduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(to='creamUsers.Product')),
                ('skinuser', models.ForeignKey(to='creamUsers.Skinuser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
