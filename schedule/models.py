from django.db import models

# route model
class Route(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# stopage and bus schedule model
class BusSchedule(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='schedules')
    stopage = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    direction = models.CharField(max_length=50, default="Campus-bound")

    def __str__(self):
        return f"{self.stopage} - {self.time}"