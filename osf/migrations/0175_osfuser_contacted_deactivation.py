# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-13 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0174_add_ab_testing_home_page_version_b_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='osfuser',
            name='contacted_deactivation',
            field=models.BooleanField(default=False),
        ),
    ]
