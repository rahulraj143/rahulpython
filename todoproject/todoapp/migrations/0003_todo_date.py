# Generated by Django 4.1.3 on 2022-12-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_prio_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default='1993-04-23'),
            preserve_default=False,
        ),
    ]