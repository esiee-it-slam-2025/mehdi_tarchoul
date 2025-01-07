// Fonction pour vérifier la validité du billet
async function checkTicketValidity(ticketId) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/check-ticket/${ticketId}/`);
        if (!response.ok) {
            throw new Error('Erreur lors de la vérification du billet');
        }
        const ticket = await response.json();

        if (ticket.valid) {
            // Afficher les informations du billet
            displayTicketInfo(ticket);
        } else {
            alert('Billet invalide : ' + ticket.error);
        }
    } catch (error) {
        console.error('Erreur :', error);
        alert('Erreur lors de la vérification du billet.');
    }
}

// Fonction pour afficher les informations du billet
function displayTicketInfo(ticket) {
    document.getElementById('scanner-section').style.display = 'none';
    document.getElementById('ticket-info').style.display = 'block';

    document.getElementById('supporter-name').textContent = ticket.supporter_name;
    document.getElementById('seat-number').textContent = ticket.seat_number;
    document.getElementById('event-name').textContent = ticket.event_name;
}