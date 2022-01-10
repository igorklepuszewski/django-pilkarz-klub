from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from .models import Pilkarz, Klub
from .forms import PilkarzForm
# Create your views here.
from .serializers import UserSerializer, GroupSerializer, PilkarzSerializer, KlubSerializer


def pilkarz(request):
    template = "pilkarz.html"
    context = {}
    context['form'] = PilkarzForm()
    if request.method == "GET":
        pilkarze = Pilkarz.objects.all()
        context['pilkarze'] = pilkarze
        return render(request, template, context)
    if request.method == "POST":
        form = PilkarzForm(request.POST)
        if form.is_valid():
            imie = form.cleaned_data["imie"]
            nazwisko = form.cleaned_data["nazwisko"]
            klub = form.cleaned_data["klub"]
            pilkarz = Pilkarz(imie=imie, nazwisko=nazwisko, klub=klub)
            pilkarz.save()
            return redirect('pilkarz')
        else:
            context['form'] = form
            return render(request, template, context)

def pilkarz_detail(request, pk):
    template="pilkarz_detail.html"
    context={}
    context["form"] = PilkarzForm()
    if request.method == "GET":
        pilkarz = Pilkarz.objects.get(id=pk)
        context["pilkarz"] = pilkarz
        return render(request, template, context)
    if request.method == "POST":
        form = PilkarzForm(request.POST)
        if form.is_valid():
            pilkarz = Pilkarz.objects.get(id=pk)
            pilkarz.imie = form.cleaned_data["imie"]
            pilkarz.nazwisko = form.cleaned_data["nazwisko"]
            pilkarz.klub = form.cleaned_data["klub"]
            pilkarz.save()
            return redirect("pilkarz")
        else:
            context['form'] = form
            return render(request, template, context)



def pilkarz_delete(request, pk):
    if request.method == "POST":
        pilkarz = Pilkarz.objects.get(id=pk)
        pilkarz.delete()
        return redirect('pilkarz')



# GET -> wziac dane
# POST -> wyslac dane na serwer, najczesciej utworzyc nowy obiekt w bazie danych
# PUT -> wyslac dane w celu zmiany obiektu
# DELETE -> usunac dane w bazie danych

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PilkarzViewSet(viewsets.ModelViewSet):
    queryset = Pilkarz.objects.all()
    serializer_class = PilkarzSerializer
    permission_classes = [permissions.IsAuthenticated]


class KlubViewSet(viewsets.ModelViewSet):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer
    permission_classes = [permissions.IsAuthenticated]

