# Generated by Django 2.0.2 on 2018-03-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_auto_20180305_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='active',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]