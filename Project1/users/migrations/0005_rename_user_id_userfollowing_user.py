# Generated by Django 4.1.2 on 2022-10-29 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfollowing',
            old_name='user_id',
            new_name='user',
        ),
    ]
