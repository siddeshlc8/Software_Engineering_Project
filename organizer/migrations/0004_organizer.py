# Generated by Django 2.0.2 on 2018-02-19 16:10

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('organizer', '0003_auto_20180219_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nationality', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
