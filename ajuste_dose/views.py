from django.shortcuts import render
from django.views import View
from .forms import ClCrForm


class ClearenceCreatinina(View):

    def get(self, request):
        clcr = None
        form = ClCrForm()
        return render(request, 'ajuste_dose/ajuste_dose.html', {'form': form, 'clcr': clcr})

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
        form = ClCrForm(request.POST)
        return render(request, 'ajuste_dose/ajuste_dose.html', {'form': form, 'clcr': clcr})
