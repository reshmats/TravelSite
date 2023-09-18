from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length=250)
    team_img = models.ImageField(upload_to='pictures')
    team_desc = models.TextField()

    def __str__(self):
        return self.team_name

