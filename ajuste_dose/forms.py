from django import forms

SEXOS = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
)


class ClCrForm(forms.Form):
    sexo = forms.ChoiceField(required=True, choices=SEXOS, label='Sexo ')
    peso = forms.FloatField(required=True, label='Peso (Kg)')
    idade = forms.IntegerField(required=True,min_value=1, label='Idade (anos)')
    creatinina = forms.FloatField(required=True,min_value=0.1 , label='Creatinina')

