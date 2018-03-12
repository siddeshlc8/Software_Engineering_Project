# Generated by Django 2.0.3 on 2018-03-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0010_remove_player_team'),
        ('tournament', '0021_team_players_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player10',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player11',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player8',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player9',
        ),
        migrations.RemoveField(
            model_name='team',
            name='players_count',
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='player.Player'),
        ),
    ]