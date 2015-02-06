# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creamUsers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question1', models.CharField(max_length=20)),
                ('question2', models.CharField(max_length=20)),
                ('question3', models.CharField(max_length=20)),
                ('question4', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('inType', models.CharField(max_length=20)),
                ('ingreName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(max_digits=18, verbose_name='price', decimal_places=2)),
                ('ingrediant1', models.ForeignKey(to='creamUsers.Ingredients', related_name='ingrediant_cream')),
                ('ingrediant2', models.ForeignKey(to='creamUsers.Ingredients', related_name='ingrediant_penetrate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
