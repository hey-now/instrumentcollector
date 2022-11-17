from django.db import models
from django.urls import reverse

PLAYED = (
    ('A', '15 mins'),
    ('B', '30 mins'),
    ('C', '1 hour'),
    ('D', '1.5 hours'),
    ('E', '2 hours')
)
# Create your models here.

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Instrument(models.Model):
    nickname = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    manf_date = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

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
    
    class Meta:
        ordering = ['-date']