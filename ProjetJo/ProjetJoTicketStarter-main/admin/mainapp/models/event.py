from django.db import models
from .team import Team
from .stadium import Stadium

STAGE_CHOICES = (
    ('Groupe', 'Groupe'),
    ('Quarts', 'Quarts'),
    ('Demi', 'Demi'),
    ('Finale', 'Finale'),
)

class Event(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.PROTECT)
    team_home = models.ForeignKey(Team, on_delete=models.PROTECT, null=True, related_name="events_as_home")
    team_away = models.ForeignKey(Team, on_delete=models.PROTECT, null=True, related_name="events_as_away")
    start = models.DateTimeField()
    score = models.CharField(max_length=10, blank=True, null=True)
    winner = models.ForeignKey(Team, on_delete=models.PROTECT, null=True, related_name="events_winner")
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES, default='Huitiemes')

    def __str__(self):
        return f"{self.start} au {self.stadium}"
