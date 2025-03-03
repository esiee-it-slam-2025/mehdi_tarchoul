from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from mainapp.models import Event, Stadium, Team

# Dictionnaire qui définit le prochain stage à partir du stage actuel.
# Ici, on considère que l'arborescence passe de Groupe → Quarts → Demi → Finale.
STAGE_ORDER = {
    "Groupe": "Quarts",
    "Quarts": "Demi",
    "Demi": "Finale",
    # Si Finale est le dernier stage, on n'a pas de prochain stage
    "Finale": None,
}

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_events(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        winner_name = request.POST.get('winner')  # Nom de l'équipe gagnante
        stadium_id = request.POST.get('stadium')    # ID du stade sélectionné
        start = request.POST.get('start')           # Nouvelle date

        try:
            event = Event.objects.get(id=event_id)
            old_winner = event.winner  # Sauvegarde de l'ancien vainqueur

            # Mise à jour du stade et de la date
            if stadium_id:
                try:
                    stadium = Stadium.objects.get(id=stadium_id)
                    event.stadium = stadium
                except Stadium.DoesNotExist:
                    messages.error(request, "Stade non trouvé.")
                    return redirect('admin_events')
            if start:
                event.start = start

            # Mise à jour du vainqueur
            if winner_name:
                try:
                    new_winner = Team.objects.get(name=winner_name)
                    event.winner = new_winner
                except Team.DoesNotExist:
                    messages.error(request, "Équipe non trouvée.")
                    return redirect('admin_events')
            else:
                new_winner = None
                event.winner = None

            event.save()
            # Mise à jour du match du prochain tour selon les trois cas
            update_next_stage_participation(event, old_winner, new_winner)
            messages.success(request, "Événement mis à jour avec succès.")
        except Event.DoesNotExist:
            messages.error(request, "Événement non trouvé.")

        return redirect('admin_events')

    # Pour un GET, on récupère les événements et les stades en BDD
    events = Event.objects.all()
    stadiums = Stadium.objects.all()
    return TemplateResponse(request, "admin_view/events.html", {"events": events, "stadiums": stadiums})

def update_next_stage_participation(current_event, old_winner, new_winner):
    """
    Met à jour le match du prochain tour en fonction du changement du vainqueur.
    Trois cas :
      1. Aucun vainqueur précédent et nouveau vainqueur → ajouter new_winner.
      2. Vainqueur retiré → retirer old_winner du prochain tour.
      3. Changement de vainqueur (old_winner != new_winner) → remplacer old_winner par new_winner.
    """
    next_stage = STAGE_ORDER.get(current_event.stage)
    if not next_stage:
        # Pas de prochain stage (exemple : Finale)
        return

    if old_winner is None and new_winner is not None:
        # Cas 1 : nouveau vainqueur, on l'ajoute
        assign_team_to_next_stage(new_winner, next_stage)
    elif old_winner is not None and new_winner is None:
        # Cas 2 : retrait du vainqueur, on retire l'ancien vainqueur
        remove_team_from_next_stage(old_winner, next_stage)
    elif old_winner is not None and new_winner is not None and old_winner != new_winner:
        # Cas 3 : changement de vainqueur, on remplace old_winner par new_winner
        update_team_in_next_stage(old_winner, new_winner, next_stage)
    # Si old_winner == new_winner, rien ne change

def assign_team_to_next_stage(team, stage):
    """
    Assigne l'équipe au prochain match (dans la première case libre : team_home ou team_away).
    """
    # Vérifie si l'équipe est déjà assignée
    if Event.objects.filter(stage=stage, team_home=team).exists() or \
       Event.objects.filter(stage=stage, team_away=team).exists():
        return

    # Cherche un match du prochain stage avec un slot libre pour team_home
    next_event = Event.objects.filter(stage=stage, team_home__isnull=True).first()
    if next_event:
        next_event.team_home = team
        next_event.save()
    else:
        # Sinon, cherche pour team_away
        next_event = Event.objects.filter(stage=stage, team_away__isnull=True).first()
        if next_event:
            next_event.team_away = team
            next_event.save()

def remove_team_from_next_stage(team, stage):
    """
    Retire l'équipe du match du prochain tour (en la remplaçant par NULL).
    """
    # Cherche dans team_home
    next_event = Event.objects.filter(stage=stage, team_home=team).first()
    if next_event:
        next_event.team_home = None
        next_event.save()
        return
    # Sinon, cherche dans team_away
    next_event = Event.objects.filter(stage=stage, team_away=team).first()
    if next_event:
        next_event.team_away = None
        next_event.save()

def update_team_in_next_stage(old_team, new_team, stage):
    """
    Dans le match du prochain tour, remplace old_team par new_team.
    """
    # Cherche d'abord si old_team est en team_home
    next_event = Event.objects.filter(stage=stage, team_home=old_team).first()
    if next_event:
        next_event.team_home = new_team
        next_event.save()
        return
    # Sinon, cherche si old_team est en team_away
    next_event = Event.objects.filter(stage=stage, team_away=old_team).first()
    if next_event:
        next_event.team_away = new_team
        next_event.save()
