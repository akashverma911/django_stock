# Generated by Django 3.2.4 on 2022-01-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_common'),
    ]

    operations = [
        migrations.AlterField(
            model_name='common',
            name='FACE_VALUE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='smeequity',
            name='FACE_VALUE',
            field=models.IntegerField(),
        ),
    ]
