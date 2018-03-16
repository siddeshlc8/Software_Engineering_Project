from django.db import models
from organizer.models import Organizer
from player.models import Player
from performance.models import PerformanceMatchWise, PerformanceMatch


# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=20, unique=True)
    place = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(default=None)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    tournament_status = models.IntegerField(default=0)
    tournament_schedule = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)
    owner = models.CharField(max_length=20)
    logo = models.ImageField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name


class Match(models.Model):
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    team_1 = models.ForeignKey('Team', related_name='team_1',on_delete=models.DO_NOTHING)
    team_2 = models.ForeignKey('Team', related_name='team_2',on_delete=models.DO_NOTHING)
    overs = models.IntegerField()
    match_status = models.IntegerField(default=0)
    winner = models.ForeignKey('Team', related_name='winner',on_delete=models.DO_NOTHING)
    toss_winner = models.ForeignKey('Team', related_name='toss_winner', on_delete=models.DO_NOTHING,
                                    blank=True, null=True)
    toss_winner_choice = models.CharField(max_length=10, default='Select')
    toss_stored = models.BooleanField(default=False)
    team_1_score = models.BigIntegerField(default=0)
    team_2_score = models.BigIntegerField(default=0)
    team_2_wickets = models.IntegerField(default=0)
    team_1_wickets = models.IntegerField(default=0)
    openers_selected_innings1 = models.BooleanField(default=False)
    openers_selected_innings2 = models.BooleanField(default=False)
    striker_innings1 = models.ForeignKey(PerformanceMatch, related_name='striker_innings1',
                                         on_delete=models.DO_NOTHING, blank=True, null=True)
    non_striker_innings1 = models.ForeignKey(PerformanceMatch, related_name='non_striker_innings1',
                                             on_delete=models.DO_NOTHING, blank=True, null=True)
    striker_innings2 = models.ForeignKey(PerformanceMatch, related_name='striker_innings2',
                                         on_delete=models.DO_NOTHING, blank=True, null=True)
    non_striker_innings2 = models.ForeignKey(PerformanceMatch, related_name='non_striker_innings2',
                                             on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return '  ' + self.team_1.name + '  vs  ' + self.team_2.name


class Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True, blank=True)
    innings = models.CharField(max_length=11)
    batting_team = models.ForeignKey('Team', related_name='batting_team', on_delete=models.DO_NOTHING, null=True, blank=True)
    bowling_team = models.ForeignKey('Team', related_name='bowling_team', on_delete=models.DO_NOTHING, null=True, blank=True)
    ball_number = models.IntegerField(null=True, blank=True)
    over_number = models.IntegerField(null=True, blank=True)
    bowler = models.ForeignKey('player.Player', related_name='bowler', null=True, on_delete=models.DO_NOTHING)
    batsman = models.ForeignKey('player.Player',related_name='batsman', null=True,
                                on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=500, null=True, blank=True)
    wicket = models.BooleanField(default=False)
    six = models.BooleanField(default=False)
    four = models.BooleanField(default=False)
    is_highlight = models.BooleanField(default=False)
    highlight = models.CharField(max_length=20, null=True, blank=True)
    out_batsman = models.ForeignKey('player.Player', related_name='out_batsman', null=True, blank=True,
                                    on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.over_number) + '.' + str(self.ball_number)


class ScoreCard(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=True, null=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True)
    team_1 = models.ForeignKey(Team, related_name='team1', on_delete=models.DO_NOTHING, null=True, blank=True)
    team_2 = models.ForeignKey(Team, related_name='team2', on_delete=models.DO_NOTHING, null=True, blank=True)
    team_1_players = models.ManyToManyField(PerformanceMatch, related_name='team_1_players')
    team_2_players = models.ManyToManyField(PerformanceMatch, related_name='team_2_players')









