# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('creamUsers', '0006_userproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('invoicenum', models.IntegerField(default=0)),
                ('isPaid', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='creamUsers.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='skinuser',
            name='user',
            field=models.OneToOneField(related_name='skinuser', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
