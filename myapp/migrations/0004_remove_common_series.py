# Generated by Django 3.2.4 on 2022-01-30 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220131_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='common',
            name='SERIES',
        ),
    ]
