# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 17:29
from __future__ import unicode_literals

from django.db import migrations
import osf.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0064_auto_20171019_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='preprintservice',
            name='original_publication_date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
    ]
