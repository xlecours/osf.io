# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-07 15:57
from __future__ import unicode_literals

import logging

from django.db import migrations
from django.apps import apps
from django.core.paginator import Paginator

from osf.models import OSFUser
from addons.osfstorage.models import Region, UserSettings as OsfStorageUserSettings
from addons.osfstorage.settings import DEFAULT_REGION_NAME, DEFAULT_REGION_ID
from website.settings import WATERBUTLER_URL

logger = logging.getLogger(__file__)

osfstorage_config = apps.get_app_config('addons_osfstorage')


def add_osfstorage_addon(*args):

    default_region, created = Region.objects.get_or_create(
        _id = DEFAULT_REGION_ID,
        name=DEFAULT_REGION_NAME,
        waterbutler_credentials=osfstorage_config.WATERBUTLER_CREDENTIALS,
        waterbutler_settings=osfstorage_config.WATERBUTLER_SETTINGS,
        waterbutler_url=WATERBUTLER_URL
    )

    if created:
        logger.info('Created default region: {}'.format(DEFAULT_REGION_NAME))

    total_users = OSFUser.objects.all().count()
    users_done = 0
    paginator = Paginator(OSFUser.objects.all(), 1000)
    for page_num in paginator.page_range:
        page = paginator.page(page_num)

        user_settings_to_update = []
        for user in page:
            new_user_settings = OsfStorageUserSettings(
                owner=user,
                default_region=default_region
            )
            user_settings_to_update.append(new_user_settings)
            users_done += 1

        OsfStorageUserSettings.objects.bulk_create(user_settings_to_update)
        logger.info('Updated {}/{} users'.format(users_done, total_users))

    logger.info('Created UserSettings for {} users'.format(total_users))


def remove_osfstorage_addon(*args):
    OsfStorageUserSettings = osfstorage_config.user_settings

    region = Region.objects.filter(
        name=DEFAULT_REGION_NAME
    )

    if region:
        region.get().delete()

    OsfStorageUserSettings.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0084_merge_20180308_1821'),
    ]

    operations = [
        migrations.RunPython(add_osfstorage_addon, remove_osfstorage_addon),
    ]
