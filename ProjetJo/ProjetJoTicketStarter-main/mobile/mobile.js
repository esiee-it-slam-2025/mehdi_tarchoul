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
        observer.observe(eventItem);
    });
    
}

// Vérifie si l'utilisateur est authentifié en regardant dans localStorage
function updateAuthUI() {
    const isAuthenticated = localStorage.getItem('authenticated') === 'true';
    if (isAuthenticated) {
        // Masquer les boutons inscription/connexion
        document.getElementById('auth-buttons').style.display = 'none';
        // Afficher le bouton de déconnexion
        document.getElementById('logout-container').style.display = 'block';
        // Rediriger automatiquement vers la liste des matchs si on se trouve sur la page de login
        // (Ici, on suppose que la liste des matchs est toujours affichée dans #event-list)
        document.getElementById('event-list').style.display = 'block';
        document.getElementById('register-form').style.display = 'none';
        document.getElementById('login-form').style.display = 'none';
    } else {
        // Utilisateur non authentifié : afficher les boutons inscription/connexion
        document.getElementById('auth-buttons').style.display = 'block';
        document.getElementById('logout-container').style.display = 'none';
    }
    
}

document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('authenticated') === 'true') {
        document.getElementById('event-list').style.display = 'block';
    }
});

// Appel initial pour mettre à jour l'interface selon l'état d'authentification
updateAuthUI();

// Modification du gestionnaire de connexion pour enregistrer l'état authentifié
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
            // On enregistre l'état authentifié
            localStorage.setItem('authenticated', 'true');
            // Mettre à jour l'UI et rediriger sur la liste des matchs
            updateAuthUI();
            // Redirection implicite : on affiche la liste des matchs
            document.getElementById('event-list').style.display = 'block';
        } else {
            alert(data.error || 'Erreur lors de la connexion');
        }
    } catch (error) {
        console.error('Erreur :', error);
        alert('Une erreur s\'est produite lors de la connexion.');
    }
});

// Fonction de déconnexion : on supprime le flag et on rafraîchit la page
function logout() {
    localStorage.removeItem('authenticated');
    alert('Déconnexion réussie');
    location.reload(); // Recharge la page pour réafficher les boutons inscription/connexion
}

// Lors du chargement de la page, on redirige si l'utilisateur est déjà connecté
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('authenticated') === 'true') {
        // L'utilisateur est connecté, on affiche la liste des matchs directement
        document.getElementById('event-list').style.display = 'block';
    }
});


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
    
    if (response.ok) {
        alert(data.message);
        // Enregistre l'état authentifié
        localStorage.setItem('authenticated', 'true');
        // Met à jour l'interface utilisateur
        updateAuthUI();
        // Affiche la liste des matchs
        document.getElementById('event-list').style.display = 'block';
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

    // Définition de la taille du QR Code et de la marge blanche
    const qrSize = 128;
    const marginSize = 20; // Marge blanche autour du QR Code

    // Création d'un canvas plus grand pour inclure la marge
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    canvas.width = qrSize + 2 * marginSize;
    canvas.height = qrSize + 2 * marginSize;

    // Remplissage du fond en blanc
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Génération du QR Code temporaire dans un div caché
    const tempDiv = document.createElement('div');
    new QRCode(tempDiv, {
        text: ticketId.toString(),
        width: qrSize,
        height: qrSize,
        colorDark: "#000000",
        colorLight: "#FFFFFF",
        correctLevel: QRCode.CorrectLevel.H
    });

    // Attente de la génération du QR Code
    setTimeout(() => {
        const qrImg = tempDiv.querySelector("img");
        if (qrImg) {
            const qrImage = new Image();
            qrImage.src = qrImg.src;
            qrImage.onload = () => {
                // Dessin du QR Code sur le canvas avec la marge blanche
                ctx.drawImage(qrImage, marginSize, marginSize, qrSize, qrSize);
                qrCodeElement.innerHTML = ''; // Supprime l'ancien QR
                qrCodeElement.appendChild(canvas); // Ajoute le nouveau QR avec marge

                // Ajoute l'événement de téléchargement
                document.getElementById('download-qr').onclick = () => {
                    const link = document.createElement('a');
                    link.href = canvas.toDataURL("image/png");
                    link.download = 'ticket_qr_code.png';
                    link.click();
                };
            };
        }
    }, 100);

    // Affichage de la section QR Code
    document.getElementById('qr-code-section').style.display = 'block';
}


// Gestionnaire d'événements pour télécharger le QR Code
document.getElementById('download-qr').addEventListener('click', () => {
    const qrCanvas = document.getElementById('qr-code').querySelector("canvas");
    if (qrCanvas) {
        const link = document.createElement('a');
        link.href = qrCanvas.toDataURL("image/png"); // Convertir en image
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

// Animation des éléments (cards) au scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

// Appliquer l'observateur à chaque élément avec la classe 'event-item'
document.querySelectorAll('.event-item').forEach(item => {
    observer.observe(item);
});


