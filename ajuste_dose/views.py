from django.shortcuts import render
from django.views import View
from .forms import ClCrForm
from .doses_dos_atbs import doses_dos_atbs, lista_atbs
from collections import OrderedDict


class ClearenceCreatinina(View):

    @staticmethod
    def dosing(atb, clcr=None):
        doses = doses_dos_atbs
        clcr = 0.01 if clcr == 'HD' else clcr
        clcr = 999 if not clcr else clcr
        dose_final = None
        dose = doses[atb]
        for k, v in dose['dosing'].items():
            if clcr < k:
                dose_final = v
                break
        dose_final_dict = {'nome': dose['nome'], 'obs': dose_final[2], 'dose': dose_final[0], 'intervalo': dose_final[1]}
        return dose_final_dict

    @staticmethod
    def dose_dict(clcr):
        atbs = lista_atbs
        dose_dict = dict()
        for atb in atbs:
            dose_dict[atb] = ClearenceCreatinina.dosing(atb, clcr)
        dose_dict = dict(sorted(dose_dict.items(), key=lambda x: x[1]['nome']))
        return dose_dict

    def get(self, request):
        form = ClCrForm()
        if request.GET.get('hd') == 'sim':
            clcr = 'HD'
        else:
            clcr = None
        dose_dict = self.dose_dict(clcr)
        return render(request, 'ajuste_dose/ajuste_dose.html', {'form': form, 'clcr': clcr, 'dose_dict': dose_dict})

    def post(self, request):
        form = ClCrForm(request.POST)
        clcr = None
        if form.is_valid():
            peso = form.cleaned_data['peso']
            idade = form.cleaned_data['idade']
            creatinina = form.cleaned_data['creatinina']
            sexo = form.cleaned_data['sexo']
            clcr = (140-idade)*peso/(72*creatinina)
            if sexo == "Feminino":
                clcr = clcr*0.85
        dose_dict = self.dose_dict(clcr)
        form = ClCrForm(request.POST)
        return render(request, 'ajuste_dose/ajuste_dose.html', {'form': form, 'clcr': clcr, 'dose_dict': dose_dict})
