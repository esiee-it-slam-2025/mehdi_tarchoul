// Fonction pour récupérer et afficher les matchs
async function fetchEvents() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/events/');
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des matchs');
        }
        const events = await response.json();
        displayEvents(events);
    } catch (error) {
        console.error('Erreur lors de la récupération des matchs :', error);
        alert('Impossible de charger les matchs. Veuillez réessayer plus tard.');
    }
}

// Fonction pour afficher les matchs dans l'interface
function displayEvents(events) {
    const eventList = document.getElementById('event-list');
    eventList.innerHTML = ''; // Vide la liste avant de la remplir

    events.forEach(event => {
        const eventItem = document.createElement('div');
        eventItem.className = 'event-item';
        eventItem.innerHTML = `
            <h3>${event.team_home} vs ${event.team_away}</h3>
            <p>Stade : ${event.stadium}</p>
            <p>Date : ${new Date(event.start).toLocaleString()}</p>
            <button onclick="showTicketForm(${event.id})">Acheter un billet</button>
        `;
        eventList.appendChild(eventItem);
    });
}

// Fonction pour afficher le formulaire d'achat de billet
function showTicketForm(eventId) {
    document.getElementById('event-list').style.display = 'none';
    document.getElementById('ticket-form').style.display = 'block';

    // Enregistre l'ID de l'événement pour l'achat
    document.getElementById('ticket-form').dataset.eventId = eventId;
}

// Fonction pour cacher le formulaire d'achat de billet
function hideTicketForm() {
    document.getElementById('ticket-form').style.display = 'none';
    document.getElementById('event-list').style.display = 'block';
}

// Gestionnaire d'événements pour l'inscription
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password }),
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);
        } else {
            alert(data.error || 'Erreur lors de l\'inscription');
        }
    } catch (error) {
        console.error('Erreur :', error);
        alert('Une erreur s\'est produite lors de l\'inscription.');
    }
});

// Gestionnaire d'événements pour la connexion
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message);
        } else {
            alert(data.error || 'Erreur lors de la connexion');
        }
    } catch (error) {
        console.error('Erreur :', error);
        alert('Une erreur s\'est produite lors de la connexion.');
    }
});

// Gestionnaire d'événements pour l'achat de billet
document.getElementById('ticket-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const category = document.getElementById('category').value;
    const eventId = document.getElementById('ticket-form').dataset.eventId;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/buy-ticket/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Nécessaire pour Django CSRF
            },
            body: JSON.stringify({ event_id: eventId, category }),
        });

        if (response.ok) {
            const ticket = await response.json();
            alert('Billet acheté avec succès !');
            generateQRCode(ticket.id);
        } else {
            const errorData = await response.json();
            alert(errorData.error || 'Erreur lors de l\'achat du billet');
        }
    } catch (error) {
        console.error('Erreur :', error);
        alert('Une erreur s\'est produite lors de l\'achat du billet.');
    }
});

// Fonction pour générer un QR Code
function generateQRCode(ticketId) {
    const qrCodeElement = document.getElementById('qr-code');
    qrCodeElement.innerHTML = ''; // Vide le contenu précédent

    new QRCode(qrCodeElement, {
        text: ticketId.toString(),
        width: 128,
        height: 128,
    });

    document.getElementById('qr-code-section').style.display = 'block';
}

// Gestionnaire d'événements pour télécharger le QR Code
document.getElementById('download-qr').addEventListener('click', () => {
    const qrCodeElement = document.getElementById('qr-code').querySelector('img');
    if (qrCodeElement) {
        const link = document.createElement('a');
        link.href = qrCodeElement.src;
        link.download = 'ticket_qr_code.png';
        link.click();
    } else {
        alert('Aucun QR Code à télécharger.');
    }
});

// Fonction pour obtenir le cookie CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Afficher le formulaire d'inscription
function showRegisterForm() {
    document.getElementById('register-form').style.display = 'block';
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('event-list').style.display = 'none';
}

// Afficher le formulaire de connexion
function showLoginForm() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('event-list').style.display = 'none';
}

// Cacher les formulaires d'authentification
function hideAuthForms() {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('event-list').style.display = 'block';
}

// Cacher la section QR Code et revenir à la liste des matchs
function hideQRCodeSection() {
    document.getElementById('qr-code-section').style.display = 'none';
    document.getElementById('event-list').style.display = 'block';
}

// Appel initial pour charger les matchs au démarrage
fetchEvents();