# Generated by Django 2.1.3 on 2018-11-15 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20181115_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_default',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
