# Generated by Django 4.2.7 on 2023-11-25 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0009_auto_20230629_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='uid',
        ),
    ]
