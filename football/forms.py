from django.contrib.auth.models import User
from django import forms
from football.models import footballClub, footballPlayers

class FootballclubForm(forms.ModelForm):
    
    class Meta:
        model = footballClub
        fields = ['clubName', 'clubJersey', 'clubLeague', 'clubBadge']

class FootballplayerForm(forms.ModelForm):
    
    class Meta:
        model = footballPlayers
        fields = ['playerName', 'playernationality', 'footballclub', 'shirtNumber', 'playerStrengths', 'playerWeakness']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']