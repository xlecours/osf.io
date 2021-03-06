# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0052_preprintprovider_share_publish_type'),
    ]

    operations = [
        migrations.RunSQL([
            'CREATE INDEX nodelog__node_id_date_desc on osf_nodelog (node_id, date DESC);',
            # 'VACUUM ANALYZE osf_nodelog;'  # Run this manually, requires ~3 min downtime
        ], [
            'DROP INDEX IF EXISTS nodelog__node_id_date_desc RESTRICT;',
        ])
    ]
