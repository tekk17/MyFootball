from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User

from django.db import models
#from django.template.defaultfilters import default

class footballClub(models.Model):
    user = models.ForeignKey(User, default=1)
    clubName = models.CharField(max_length=200)
    clubJersey = models.CharField(max_length=50)
    clubLeague = models.CharField(max_length=50)
    clubBadge = models.FileField()
    
    def get_absolute_url(self):
        return reverse('football:detail', kwargs={'pk' : self.pk})
    
    def __str__(self):
        return self.clubName + ' - ' + self.clubLeague
    
#class playingPosition(models.Model):
#    positionName = models.CharField(max_length=100)
#    
#    def __str__(self):
#        return self.positionName

class footballPlayers(models.Model):
    playerName = models.CharField(max_length=100)
    playernationality = models.CharField(max_length=50)
    footballclub = models.ForeignKey(footballClub, on_delete=models.CASCADE)
    shirtNumber = models.CharField(max_length=100,default='')
    playerStrengths = models.CharField(max_length=1000,default='')
    playerWeakness = models.CharField(max_length=1000,default='')
    
    def get_absolute_url(self):
        return reverse('football:detail', kwargs={'pk' : self.footballclub.pk})
    
    def __str__(self):
        #return self.playerName + ' - ' + self.footballclub
        return self.playerName
