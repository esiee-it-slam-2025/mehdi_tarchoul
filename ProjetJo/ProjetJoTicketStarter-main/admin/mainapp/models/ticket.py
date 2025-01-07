from django.db import models
from uuid import uuid4
from .event import Event

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinium', 'Platinium')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supporter_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Ticket pour {self.event} ({self.category})"