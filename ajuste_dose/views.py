from django.shortcuts import render
from django.views import View
from .forms import ClCrForm


def amp_sulb(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 3000
        resultado['intervalo'] = 24
        resultado['obs'] = 'No dia da HD, administrar a dose após a HD'
    elif clcr < 10:
        resultado['dose'] = 3000
        resultado['intervalo'] = 24
    elif 10 <= clcr <= 50:
        resultado['dose'] = 3000
        resultado['intervalo'] = 12
    else:
        resultado['dose'] = 3000
        resultado['intervalo'] = 6
    return resultado


def amx_clv_oral(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 500
        resultado['intervalo'] = 24
        resultado['obs'] = 'No dia da HD, administrar uma dose extra após a HD'
    elif clcr < 10:
        resultado['dose'] = 500
        resultado['intervalo'] = 24
    elif 10 <= clcr <= 50:
        resultado['dose'] = 500
        resultado['intervalo'] = 12
    else:
        resultado['dose'] = 500
        resultado['intervalo'] = 8
    return resultado


def amx_clv_iv(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 500
        resultado['intervalo'] = 24
        resultado['obs'] = 'No dia da HD, administrar uma dose extra após a HD'
    elif clcr < 10:
        resultado['dose'] = 500
        resultado['intervalo'] = 24
    elif 10 <= clcr <= 30:
        resultado['dose'] = 500
        resultado['intervalo'] = 12
    else:
        resultado['dose'] = 500
        resultado['intervalo'] = 8
    return resultado


def aztreonam(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 2000
        resultado['intervalo'] = 24
        resultado['obs'] = 'No dia da HD, administrar a dose após a HD'
    elif clcr < 10:
        resultado['dose'] = 2000
        resultado['intervalo'] = 24
    elif 10 <= clcr <= 50:
        resultado['dose'] = 1000
        resultado['intervalo'] = 8
    else:
        resultado['dose'] = 2000
        resultado['intervalo'] = 8
    return resultado


def cefazolina(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 2000
        resultado['intervalo'] = 24
        resultado['obs'] = 'No dia da HD, administrar a 1000mg após a HD'
    elif clcr < 10:
        resultado['dose'] = 2000
        resultado['intervalo'] = 24
    elif 10 <= clcr <= 50:
        resultado['dose'] = 1000
        resultado['intervalo'] = 12
    else:
        resultado['dose'] = 2000
        resultado['intervalo'] = 8
    return resultado


def cefepime(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 1000
        resultado['intervalo'] = 24
        resultado['obs'] = 'No dia da HD, administrar a dose após a HD'
    elif clcr < 11:
        resultado['dose'] = 1000
        resultado['intervalo'] = 24
    elif 11 <= clcr <= 29:
        resultado['dose'] = 2000
        resultado['intervalo'] = 24
    elif 30 <= clcr <= 60:
        resultado['dose'] = 2000
        resultado['intervalo'] = 12
    else:
        resultado['dose'] = 2000
        resultado['intervalo'] = 8
    return resultado


def ceftazidima(clcr = None):
    clcr = 100 if not clcr else clcr
    resultado = {'obs': ''}
    if clcr == 'HD':
        resultado['dose'] = 2000
        resultado['intervalo'] = 48
        resultado['obs'] = 'No dia da HD, administrar dose extra de 1000mg após a HD'
    elif clcr < 10:
        resultado['dose'] = 2000
        resultado['intervalo'] = 48
    elif 10 <= clcr <= 50:
        resultado['dose'] = 2000
        resultado['intervalo'] = 24
    else:
        resultado['dose'] = 2000
        resultado['intervalo'] = 8
    return resultado


class ClearenceCreatinina(View):

    def get(self, request):
        form = ClCrForm()
        if request.GET.get('hd') == 'sim':
            clcr = 'HD'
        else:
            clcr = None
        asb = amp_sulb(clcr)
        amc_oral = amx_clv_oral(clcr)
        amc_iv = amx_clv_iv(clcr)
        atm = aztreonam(clcr)
        cfz = cefazolina(clcr)
        cpm = cefepime(clcr)
        caz = ceftazidima(clcr)
        return render(request, 'ajuste_dose/ajuste_dose.html', {'form': form,
                                                                'clcr': clcr,
                                                                'asb': asb,
                                                                'amc_oral': amc_oral,
                                                                'amc_iv': amc_iv,
                                                                'atm': atm,
                                                                'cfz': cfz,
                                                                'cpm': cpm,
                                                                'caz': caz})

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
        asb = amp_sulb(clcr)
        amc_oral = amx_clv_oral(clcr)
        amc_iv = amx_clv_iv(clcr)
        atm = aztreonam(clcr)
        cfz = cefazolina(clcr)
        cpm = cefepime(clcr)
        caz = ceftazidima(clcr)
        form = ClCrForm(request.POST)
        return render(request, 'ajuste_dose/ajuste_dose.html', {'form': form,
                                                                'clcr': clcr,
                                                                'asb': asb,
                                                                'amc_oral': amc_oral,
                                                                'amc_iv': amc_iv,
                                                                'atm': atm,
                                                                'cfz': cfz,
                                                                'cpm': cpm,
                                                                'caz': caz})
