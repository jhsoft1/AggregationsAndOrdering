from django.db import models


class DayWeather(models.Model):
    date = models.DateField()
    precipitation = models.FloatField()
    temperature = models.FloatField()
    was_raining = models.BooleanField()

    def __str__(self):
        return f'{self.date} {self.precipitation} {self.temperature} {self.was_raining}'

