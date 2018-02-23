from django.shortcuts import render, redirect
from .models import Team, Tournament, Match
from player.models import Player
from .forms import TournamentCreationForm, TeamCreationForm,MatchCreationForm,ScoreForm
from django.contrib import messages
from organizer.models import Organizer
# Create your views here.


def create_tournament(request, organizer_id):
    organizer = Organizer.objects.get(pk=organizer_id)
    if request.method == 'POST':
        form = TournamentCreationForm(request.POST)
        if form.is_valid():
            new_tournament = form.save(commit=False)
            new_tournament.organizer = organizer
            new_tournament.save()
            return redirect('tournament:tournament', organizer_id)
    else:
        form = TournamentCreationForm()
        context = {'form': form, 'organizer': organizer}
        return render(request, 'tournament/tournament_templates/create_tournament.html', context)


def create_team(request, organizer_id, tournament_id):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        current_tournament = Tournament.objects.get(pk=tournament_id)
        if form.is_valid():
            team = form.save(commit=False)
            team.tournament = current_tournament
            team.save()
            return redirect('tournament:tournament_teams', organizer_id, tournament_id)
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('tournament:tournament_teams', organizer_id, tournament_id)
    else:
        form = TeamCreationForm()
        context = {'form': form}
        return render(request, 'tournament/team_templates/create_team.html', context)


def tournament(request, organizer_id):
    organizer = Organizer.objects.get(pk=organizer_id)
    all_tournament = Tournament.objects.filter(organizer=organizer)
    context = {'all_tournament': all_tournament, 'organizer':organizer}
    return render(request, 'tournament/tournament_templates/tournaments.html', context)


def tournament_teams(request, organizer_id, tournament_id):
    organizer = Organizer.objects.get(pk=organizer_id)
    current_tournament = Tournament.objects.get(pk=tournament_id)
    teams = current_tournament.team_set.all()
    context = {'current_tournament': current_tournament, 'teams': teams, 'organizer': organizer}
    return render(request, 'tournament/team_templates/tournament_teams.html', context)


def team_players(request, team_id):
    current_team = Team.objects.get(pk=team_id)
    current_players = current_team.player_set.all()
    available_players = Player.objects.exclude(team__pk=team_id)
    context = {'current_players': current_players, 'team': current_team, 'available_players': available_players}
    return render(request, 'tournament/team_templates/team_players.html', context)


def team_players_add(request, team_id, player_id):
    team_ = Team.objects.get(pk=team_id)
    player_ = Player.objects.get(pk=player_id)
    team_.player_set.add(player_)
    return redirect('tournament:team_players', team_id)

def all_matches(request, tournament_id):
    tournament=Tournament.objects.get(id=tournament_id)
    al_matches = tournament.match_set.all()
    return render(request,'tournament/match_templates/matches.html',{'tournament':tournament,'matches':al_matches})

def create_match(request,tournament_id):
    if request.method == 'POST':
        form = MatchCreationForm(request.POST)
        tournament = Tournament.objects.get(pk=tournament_id)
        if form.is_valid():
            match = form.save(commit=False)
            match.tournament = tournament
            match.winner=match.team_1
            match.save()
            return redirect('tournament:all_matches', tournament_id)
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('tournament:create_match', tournament_id)
    else:
        form = MatchCreationForm()
        context = {'form': form}
        return render(request, 'tournament/match_templates/create_match.html', context)

def enter_score(request,tournament_id,match_id):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        match = Match.objects.get(pk=match_id)
        if form.is_valid():
            score = form.save(commit=False)
            score.match = match

            score.save()
            return redirect('tournament:scores', tournament_id,match_id)
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('tournament:enter_score', tournament_id,match_id)
    else:
        form = ScoreForm()
        context = {'form': form}
        return render(request, 'tournament/score_templates/enter_score.html', context)


def  scores(request, tournament_id,match_id):
    match=Match.objects.get(id=match_id)

    all_scores =match.score_set.all()
    return render(request,'tournament/score_templates/scores.html',{'all_scores':all_scores,'match':match,'tournament_id':tournament_id})

def  match(request, tournament_id,match_id):
    match=Match.objects.get(id=match_id)
    tournament=Tournament.objects.get(id=tournament_id)
    return render(request,'tournament/match_templates/current_match.html',{'tournament':tournament,'match':match})