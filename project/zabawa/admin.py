from django.contrib import admin
from .models import Osoba, Adres, Pilkarz, Klub, Ksiazka, Tag
# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie', 'nazwisko', 'wiek', 'samochod', 'adres']

class PilkarzAdmin(admin.ModelAdmin):
    list_display = ["id", "imie", "nazwisko", "klub"]

class KlubAdmin(admin.ModelAdmin):
    list_display = ["id", "nazwa", "kraj"]

class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ["id", "tytul"]

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'nazwa']



admin.site.register(Pilkarz, PilkarzAdmin)
admin.site.register(Klub, KlubAdmin)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Ksiazka,KsiazkaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Adres)
