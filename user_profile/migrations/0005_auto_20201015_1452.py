# Generated by Django 3.1.2 on 2020-10-15 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20201015_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='preferred_user',
            new_name='premium_user',
        ),
    ]
