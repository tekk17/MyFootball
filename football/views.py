from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm, FootballclubForm, FootballplayerForm
from .models import footballClub, footballPlayers

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_footballclub(request):
    if not request.user.is_authenticated():
        return render(request, 'football/login.html')
    else:
        form = FootballclubForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            footballclub = form.save(commit=False)
            footballclub.user = request.user
            footballclub.clubBadge = request.FILES['clubBadge']
            file_type = footballclub.clubBadge.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                           'footballclub' : footballclub,
                           'form' : form,
                           'error_message' : 'Image file must be PNG, JPG or JPEG',
                }
                return render(request, 'football/create_footballclub.html', context)
            footballclub.save()
            return render(request, 'football/detail.html', {'footballclub' : footballclub})
        context = {
                   "form" : form,
        }
        return render(request, 'football/create_footballclub.html', context)

def create_footballplayer(request,footballclub_id):
    form = FootballplayerForm(request.POST or None, request.FILES or None)
    footballclub = get_object_or_404(footballClub, pk=footballclub_id)
    if form.is_valid():
        footballclubs_footballplayers = footballclub.footballplayers_set.all()
        for p in footballclubs_footballplayers:
            if p.playerName == form.cleaned_data.get("playerName"):
                context = {
                           'footballclub' : footballclub,
                           'form' : form,
                           'error_message' : 'You have already added that player',
                }
                return render(request, 'football/create_player.html', context)
        footballplayers = form.save(commit=False)
        footballplayers.footballclub = footballclub
        footballplayers.save()
        return render(request, 'football/detail.html', {'footballclub' : footballclub})
    context = {
               'footballclub' : footballclub,
               'form' : form,
    }
    return render(request, 'football/create_footballplayer.html', context)
        
def delete_footballclub(request,footballclub_id):
    footballclub = footballClub.objects.get(pk=footballclub_id)
    footballclub.delete()
    footballclubs = footballClub.objects.filter(user=request.user)
    return render(request, 'football/index.html', {'footballclubs' : footballclubs})

def delete_footballplayer(request, footballclub_id, footballplayer_id):
    footballclub = get_object_or_404(footballClub, pk=footballclub_id)
    footballplayer = footballPlayers.objects.get(pk=footballplayer_id)
    footballplayer.delete()
    return render(request,'football/detail.html',{'footballclub':footballclub})

def detail(request, footballclub_id):
    if not request.user.is_authenticated():
        return render(request, 'football/login.html')
    else:
        user = request.user
        footballclub = get_object_or_404(footballClub,pk=footballclub_id)
        return render(request,'football/detail.html',{'footballclub':footballclub,'user':user})

def index(request):
    if not request.user.is_authenticated():
        return render(request,'football/login.html')
    else:
        footballclubs = footballClub.objects.filter(user=request.user)
        footballplayers_results = footballPlayers.objects.all()
        query = request.GET.get("q")
        if query:
            footballclubs = footballclubs.filter(
                                   Q(clubName__icontains=query) |
                                   Q(clubLeague__icontains=query)
            ).distinct()
            footballplayers_results = footballplayers_results.filter(
                                                                   Q(playerName__icontains=query)
            ).distinct()
            return render(request, 'football/index.html', {
                                                           'footballclubs' : footballclubs,
                                                           'footballplayers' : footballplayers_results,
            })
        else:
            return render(request, 'football/index.html', {'footballclubs' : footballclubs})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'football/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                footballclubs = footballClub.objects.filter(user=request.user)
                return render(request, 'football/index.html', {'footballclubs': footballclubs})
            else:
                return render(request, 'football/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'football/login.html', {'error_message': 'Invalid login'})
    return render(request, 'football/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                footballclubs = footballClub.objects.filter(user=request.user)
                return render(request, 'football/index.html', {'footballclubs': footballclubs})
    context = {
        "form": form,
    }
    return render(request, 'football/register.html', context)

def footballplayers(request,filter_by):
    if not request.user.is_authenticated():
        return render(request,'football/login.html')
    else:
        try:
            footballplayers_ids = []
            for footballclub in footballClub.objects.filter(user=request.user):
                for footballplayers in footballclub.footballplayers_set.all():
                    footballplayers_ids.append(footballplayers.pk)
            users_footballplayers = footballPlayers.objects.filter(pk__in=footballplayers_ids)
        except footballClub.DoesNotExist:
            users_footballplayers = []
        return render(request,'football/footballplayers.html',{
                                                               'footballplayers_list' : users_footballplayers,
                                                               'filter_by' : filter_by,
        })
