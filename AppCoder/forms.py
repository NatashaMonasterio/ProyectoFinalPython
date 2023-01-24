from django import forms

class VeterinariosForms(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    matricula= forms.IntegerField()

class MascotasForms(forms.Form):
    nombre= forms.CharField(max_length=30)
    raza= forms.CharField(max_length=30)
    edad= forms.IntegerField()
    peso= forms.IntegerField()
    vacunado = forms.BooleanField()

class AlimentosForms(forms.Form):
    animal= forms.CharField(max_length=30)
    nombre= forms.CharField(max_length=30)
    precio= forms.IntegerField()
    cantidad= forms.IntegerField()
