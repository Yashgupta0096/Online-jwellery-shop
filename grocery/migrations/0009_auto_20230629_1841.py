# Generated by Django 3.0.5 on 2023-06-29 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0008_profile_face_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='face_id',
            new_name='uid',
        ),
    ]
