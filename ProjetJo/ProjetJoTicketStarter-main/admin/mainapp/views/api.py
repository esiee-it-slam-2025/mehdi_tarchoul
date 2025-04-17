from django.http import JsonResponse
from ..models.team import Team
from ..models.stadium import Stadium
from ..models.event import Event
from ..models.ticket import Ticket
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
import logging


logger = logging.getLogger(__name__)


# Vue pour la liste des équipes
def team_list(request):
    teams = Team.objects.all()
    data = [{'id': team.id, 'name': team.name, 'code': team.code} for team in teams]
    return JsonResponse(data, safe=False)

# Vue pour la liste des stades
def stadium_list(request):
    stadiums = Stadium.objects.all()
    data = [{'id': stadium.id, 'name': stadium.name, 'location': stadium.location} for stadium in stadiums]
    return JsonResponse(data, safe=False)

# Vue pour la liste des événements
def event_list(request):
    events = Event.objects.all()
    data = []
    for event in events:
        try:
            event_data = {
                'id': event.id,
                'team_home': event.team_home.name,
                'team_away': event.team_away.name,
                'stadium': event.stadium.name,
                'start': event.start,
                'score': event.score,
                'winner': event.winner.name if event.winner else None
            }
            data.append(event_data)
        except Exception as e:
            logger.error(f"Erreur lors du traitement de l'événement {event.id}: {e}")
    return JsonResponse(data, safe=False)

# Vue pour la liste des tickets
def ticket_list(request):
    tickets = Ticket.objects.all()
    data = [{
        'id': str(ticket.id),  # UUID est converti en chaîne
        'event': ticket.event.id,
        'category': ticket.category,
        'price': str(ticket.price),  # Decimal est converti en chaîne
        'supporter_name': ticket.supporter_name
    } for ticket in tickets]
    return JsonResponse(data, safe=False)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not email or not password:
                return JsonResponse({'error': 'Tous les champs sont obligatoires'}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Ce nom d\'utilisateur est déjà pris'}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return JsonResponse({'message': 'Inscription réussie !'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Connexion réussie !'}, status=200)
            else:
                return JsonResponse({'error': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    
@csrf_exempt
def buy_ticket(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event_id = data.get('event_id')
            category = data.get('category')

            if not event_id or not category:
                return JsonResponse({'error': 'Tous les champs sont obligatoires'}, status=400)

            event = Event.objects.get(id=event_id)

            # Créez un nouveau billet
            ticket = Ticket(event=event, category=category, price=calculate_price(category))
            ticket.save()

            return JsonResponse({'id': ticket.id, 'message': 'Billet acheté avec succès !'}, status=201)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'Événement non trouvé'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def calculate_price(category):
    if category == 'Silver':
        return 100
    elif category == 'Gold':
        return 200
    elif category == 'Platinium':
        return 300
    else:
        return 0
    
@csrf_exempt
def check_ticket(request, ticket_id):
    if request.method == 'GET':
        try:
            # Récupérer le billet depuis la base de données
            ticket = Ticket.objects.get(id=ticket_id)

            # Récupérer les informations associées au billet
            event = ticket.event
            supporter = ticket.supporter_name  # Pour le champ "supporter" dans le modèle Ticket

            # Renvoyer les informations du billet
            return JsonResponse({
                'valid': True,
                'supporter_name': supporter,  
                'seat_number': ticket.category,  # Supposons que vous avez un champ "seat_number" dans le modèle Ticket
                'event_name': f"{event.team_home} vs {event.team_away}",  # Nom du match
            })
        except Ticket.DoesNotExist:
            return JsonResponse({'valid': False, 'error': 'Billet non trouvé'}, status=404)
        except Exception as e:
            return JsonResponse({'valid': False, 'error': str(e)}, status=500)
            
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)