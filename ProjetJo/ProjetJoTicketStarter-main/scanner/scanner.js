// Configuration du scanner
const html5QrCode = new Html5Qrcode("qr-reader");

function onScanSuccess(decodedText, decodedResult) {
    checkTicketValidity(decodedText);
}

function onScanFailure(error) {
    console.warn(`Erreur de scan: ${error}`);
}

// Démarrer le scanner
html5QrCode.start(
    { facingMode: "user" },
    { fps: 10, qrbox: 250 },
    onScanSuccess,
    onScanFailure
).catch(err => {
    console.error("Erreur lors du démarrage du scanner :", err);
    alert("Impossible d'accéder à la caméra. Vérifiez les permissions.");
});


// Gestion de l'upload d'image
document.getElementById('qr-input-file').addEventListener('change', function(e) {
    if (e.target.files.length === 0) {
        return;
    }
    const imageFile = e.target.files[0];
    html5QrCode.scanFile(imageFile, true)
        .then(decodedText => {
            checkTicketValidity(decodedText);
        })
        .catch(err => {
            console.error(`Erreur lors du scan: ${err}`);
        });
});

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

// Fonction pour réinitialiser le scanner
function resetScanner() {
    document.getElementById('scanner-section').style.display = 'block';
    document.getElementById('ticket-info').style.display = 'none';
    html5QrCode.start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        onScanSuccess,
        onScanFailure
    );
}