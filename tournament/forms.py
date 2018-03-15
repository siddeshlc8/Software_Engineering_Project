from django import forms
from .models import Team, Tournament, Match, Score
from player.models import Player
from performance.models import PerformanceMatchWise, PerformanceMatch



class TeamCreationForm(forms.ModelForm):
    logo = forms.ImageField(required=False)

    class Meta:
        model = Team
        fields = [
            'name',
            'owner',
            'logo'
        ]
        labels = {
            'name': 'Team Name',
            'owner': 'Team Owner',
            'logo': 'Team Logo'
        }


class TournamentCreationForm(forms.ModelForm):
    place = forms.CharField(widget=forms.Textarea, max_length=100)

    class Meta:
        model = Tournament
        fields = [
            'name',
            'place',
            'start_date',
            'end_date'
        ]
        labels = {
            'name': 'Tournament Name',
            'start_date': 'Tournament Starting Date',
            'end_date': 'Tournament Ending Date'
        }


class MatchCreationForm(forms.ModelForm):

    def __init__(self, tournament, *args, **kwargs):
        super(MatchCreationForm, self).__init__(*args, **kwargs)
        self.fields['team_1'] = forms.ModelChoiceField(
            queryset=Team.objects.filter(tournament=tournament)
        )
        self.fields['team_2'] = forms.ModelChoiceField(
            queryset=Team.objects.filter(tournament=tournament)
        )

    class Meta:
        model = Match
        fields = [

            'team_1',
            'team_2',
            'overs'
        ]


class ScoreUpdateForm(forms.Form):
    def __init__(self, player1, player2, bowling, match, *args, **kwargs):
        super(ScoreUpdateForm, self).__init__(*args, **kwargs)
        self.fields['bowler'] = forms.ChoiceField(
            choices=[(player.player.id, str(player.player)) for player in PerformanceMatch.objects.filter(
                match=match).filter(team=bowling)]
        )
        self.fields['batsman'] = forms.ChoiceField(
            choices=[(player1.player.id, str(player1.player)), (player2.player.id, str(player2.player))]
        )
        self.fields['out_batsman'] = forms.ChoiceField(
            choices=[(player1.player.id, str(player1.player)), (player2.player.id, str(player2.player))]
        )
        self.fields['extra_type'] = forms.ChoiceField(
            choices=[
                ('Wide', 'Wide'),
                ('NoBall', 'NoBall'),
                ('DeadBall', 'DeadBall')
            ]
        )
        self.fields['wicket_type'] = forms.ChoiceField(
            choices=[
                ('RunOut', 'RunOut'),
                ('Catch', 'Catch'),
                ('Bowled', 'Bowled'),
                ('Lbw', 'Lbw'),
                ('Stumps', 'Stumps'),
                ('HitWicket', 'HitWicket')
            ]
        )

    ball_number = forms.IntegerField()
    over_number = forms.IntegerField()
    bowler = forms.CharField(max_length=11)
    batsman = forms.CharField(max_length=11)
    run = forms.IntegerField(required=False)
    extra_type = forms.CharField(max_length=11, required=False,)
    extra_run = forms.IntegerField(required=False)
    is_wicket = forms.BooleanField(required=False)
    wicket_type = forms.CharField(max_length=11, required=False)
    six = forms.BooleanField(required=False)
    four = forms.BooleanField(required=False)
    out_batsman = forms.CharField(max_length=11)
    commentary = forms.CharField(widget=forms.Textarea(attrs={'cols': '70', 'rows': '3'}))
    is_extra = forms.BooleanField(required=False)


class SelectBatsmanForm(forms.Form):
    def __init__(self, match, team, *args, **kwargs):
        super(SelectBatsmanForm, self).__init__(*args, **kwargs)
        self.fields['player'] = forms.ChoiceField(
            choices=[(player.id, str(player)) for player in PerformanceMatch.objects.filter(
                match=match).filter(team=team).filter(batting_innings__out=False)]
        )

    player = forms.CharField(max_length=12)


class TossForm(forms.Form):
    def __init__(self, match, *args, **kwargs):
        super(TossForm, self).__init__(*args, **kwargs)
        self.fields['toss_winner'] = forms.ChoiceField(
            choices=[ (match.team_1.id, str(match.team_1)), (match.team_2.id, str(match.team_2))]
        )
        self.fields['toss_winner_choice'] = forms.ChoiceField(
            choices=[('Batting', 'Batting'),
                     ('Bowling', 'Bowling')]
        )

    toss_winner = forms.CharField(max_length=11)
    toss_winner_choice = forms.CharField(max_length=10)


class OverForm(forms.Form):
    overs = forms.IntegerField()


class OpenerForm1(forms.Form):
    def __init__(self, team, *args, **kwargs):
        super(OpenerForm1, self).__init__(*args, **kwargs)
        self.fields['striker_innings1'] = forms.ChoiceField(
            choices=[(player.id, str(player)) for player in team.players.all()]
        )
        self.fields['non_striker_innings1'] = forms.ChoiceField(
            choices=[(player.id, str(player)) for player in team.players.all()]
        )

    striker_innings1 = forms.CharField(required=False)
    non_striker_innings1 = forms.CharField(required=False)


class OpenerForm2(forms.Form):
    def __init__(self, team, *args, **kwargs):
        super(OpenerForm2, self).__init__(*args, **kwargs)
        self.fields['striker_innings2'] = forms.ChoiceField(
            choices=[(player.id, str(player)) for player in team.players.all()]
        )
        self.fields['non_striker_innings2'] = forms.ChoiceField(
            choices=[(player.id, str(player)) for player in team.players.all()]
        )

    striker_innings2 = forms.CharField(required=False)
    non_striker_innings2 = forms.CharField(required=False)
