# Generated by Django 4.2.1 on 2023-05-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_bankentity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankentity',
            name='created',
        ),
    ]
