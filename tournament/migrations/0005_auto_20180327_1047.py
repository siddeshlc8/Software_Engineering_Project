# Generated by Django 2.0.3 on 2018-03-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_tournament_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='image',
            field=models.ImageField(blank=True, default='media/tournament/e.jpeg', upload_to='tournaments'),
        ),
    ]
