from django.db import models

# Create your models here.

# Stworzmy tabele Osoba ktora posiada imie i nazwisko

class Adres(models.Model):
    ulica = models.CharField(max_length=32)
    nr_dom = models.PositiveIntegerField()
    nr_miesz = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):

        return f'ul.{self.ulica} {self.nr_dom}' if self.nr_miesz is None else \
               f'ul.{self.ulica} {self.nr_dom}/{self.nr_miesz}'

class Osoba(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    wiek = models.PositiveIntegerField(default=0)
    samochod = models.CharField(max_length=32, blank=True, null=True)
    adres = models.ForeignKey(Adres, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.imie} {self.nazwisko}'

    class Meta:
        verbose_name="Osoba"
        verbose_name_plural="Osoby"

# Stworzyc tabele pilkarz o polach imie i nazwisko
# Stworzyc tabele klub o polach nazwa klubu i kraj
# Dodac relacje jeden do wielu w tabeli pilkarz (jeden pilkarz moze miec jeden klub, ale klub moze miec wielu pilkarzy)

class Klub(models.Model):
    nazwa = models.CharField(max_length=32)
    kraj = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Klub"
        verbose_name_plural = "Kluby"

    def __str__(self):
        return f'{self.nazwa}'

class Pilkarz(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    klub = models.ForeignKey(Klub, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Pilkarz"
        verbose_name_plural = "Pilkarze"

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.klub}'


# 5. Stworzyc table ksiazka, ktora posiada pola: tytul
# 6. Stworzyc tabele tag, ktora posiada pole: nazwa
# 7. Dodac relacje wiele do wielu w tabeli ksiazka z tabela tag (jedna ksiazka moze miec wiele tagow, jeden tag moze byc przypisany do wielu ksiazek)

class Tag(models.Model):
    nazwa = models.CharField(max_length=32)

    def __str__(self):

        return f'{self.nazwa}'


class Ksiazka(models.Model):
    tytul = models.CharField(max_length=32)
    tag = models.ManyToManyField(Tag, related_name="ksiazki")

    def __str__(self):
        return f'{self.tytul}'
