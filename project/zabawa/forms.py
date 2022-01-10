from .models import Pilkarz, Klub
from django import forms

class PilkarzForm(forms.ModelForm):
    imie = forms.CharField(max_length=32)
    nazwisko = forms.CharField(max_length=32)

    class Meta:
        model = Pilkarz
        fields = ('imie', 'nazwisko',)


    def __init__(self, *args, **kwargs):
        super(PilkarzForm,self).__init__(*args, **kwargs)
        self.fields['klub'] = forms.ModelChoiceField(queryset=Klub.objects.all())

