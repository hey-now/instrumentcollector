from django.db import models
from django.urls import reverse

# Create your models here.

PLAYED = (
    ('N', 'No'),
    ('Y', 'Yes')
)

class Instrument(models.Model):
    nickname = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    manf_date = models.IntegerField()

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('detail', kwargs={'instrument_id': self.id})

class Played(models.Model):
    date = models.DateField('Played on')
    played = models.CharField(
        max_length=1,
        choices=PLAYED,
        default=PLAYED[0][0]
        )

    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_played_display()} on {self.date}"