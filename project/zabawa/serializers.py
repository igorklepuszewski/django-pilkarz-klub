from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Pilkarz, Klub


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class KlubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klub
        fields = ['nazwa', 'kraj']

class PilkarzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilkarz
        fields = ['imie', 'nazwisko', "klub"]