# Generated by Django 3.2.9 on 2021-11-03 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='model_id',
            new_name='task_id',
        ),
    ]
