doses_dos_atbs = {
    'asb': {
        'nome': 'Ampicilina-Sulbactam',
        'dosing': {
            0.02: ('3000mg', '24/24h', 'No dia da HD, administrar a dose após a HD'),
            10: ('3000mg', '24/24h', ''),
            50.01: ('3000mg', '12/12h', ''),
            1000: ('3000mg', '6/6h', ''),
        }
    },
    'amc_oral': {
        'nome': 'Amoxicilina-Clavulanato (Oral)',
        'dosing': {
            0.02: ('500mg', '24/24h', 'No dia da HD, administrar uma dose extra após a HD'),
            10: ('500mg', '24/24h', ''),
            50.01: ('500mg', '12/12h', ''),
            1000: ('500mg', '8/8h', ''),
        }
    },
    'amc_iv': {
        'nome': 'Amoxicilina-Clavulanato (IV)',
        'dosing': {
            0.02: ('500mg', '24/24h', 'No dia da HD, administrar uma dose extra após a HD'),
            10: ('500mg', '24/24h', ''),
            30.01: ('500mg', '12/12h', ''),
            1000: ('500mg', '8/8h', ''),
        }
    },
    'cfz': {
        'nome': 'Cefazolina',
        'dosing': {
            0.02: ('2000mg', '24/24h', 'No dia da HD, administrar dose extra de 1000mg após a HD'),
            10: ('2000mg', '24/24h', ''),
            50.01: ('1000mg', '8/8h', ''),
            1000: ('2000mg', '8/8h', ''),
        }
    },
    'cpm': {
        'nome': 'Cefepime',
        'dosing': {
            0.02: ('1000mg', '24/24h', 'No dia da HD, administrar a dose após a HD'),
            10: ('1000mg', '24/24h', ''),
            30: ('2000mg', '24/24h', ''),
            60.01: ('2000mg', '12/12h', ''),
            1000: ('2000mg', '8/8h', ''),
        }
    },
    'caz': {
        'nome': 'Ceftazidima',
        'dosing': {
            0.02: ('2000mg', '48/48h', 'No dia da HD, administrar dose extra de 1000mg após a HD'),
            10: ('2000mg', '48/48h', ''),
            50.01: ('2000mg', '24/24h', ''),
            1000: ('2000mg', '8/8h', ''),
        }
    },
    'atm': {
        'nome': 'Aztreonam',
        'dosing': {
            0.02: ('2000mg', '24/24h', 'No dia da HD, administrar a dose após a HD'),
            10: ('2000mg', '24/24h', ''),
            50.01: ('1000mg', '8/8h', ''),
            1000: ('2000mg', '8/8h', ''),
        }
    },
    'imi': {
        'nome': 'Imipenem',
        'dosing': {
            0.02: ('500mg', '12/12h', 'Administre após HD no dia da HD'),
            30: ('500mg', '12/12h', ''),
            60: ('500mg', '8/8h', ''),
            90: ('500mg', '6/6h', ''),
            1000: ('1000mg', '8/8h', ''),
        }
    },
    'van': {
        'nome': 'Vancomicina',
        'dosing': {
            0.02: ('7.5mg/kg', '72/72h', 'A cada 48-72h, após a HD'),
            10: ('7.5mg/kg', '72/72h', 'A cada 48-72h'),
            50.01: ('15mg/kg', '48/48h', 'A cada 24-96h'),
            1000: ('1000mg', '12/12h', 'Alvo: >10-15mcg/ml'),
        }
    },
    'ppt': {
        'nome': 'Piperacilina-tazobactam',
        'dosing': {
            0.02: ('2250mg', '8/8h', 'Administre dose extra de 750mg após HD'),
            20: ('2250mg', '6/6h', ''),
            40: ('3375mg', '6/6h', ''),
            1000: ('4500mg', '6/6h', ''),
        }
    },
    'cro': {
        'nome': 'Ceftriaxone',
        'dosing': {
            0.02: ('2000mg', '24/24h', 'Sem ajuste'),
            1000: ('2000mg', '24/24h', 'Sem ajustes'),
        }
    },
    'mpm': {
        'nome': 'Meropenem',
        'dosing': {
            0.02: ('500mg', '24/24h', 'Administre após HD no dia da HD'),
            10: ('500mg', '24/24h', ''),
            25.01: ('500mg', '12/12h', ''),
            50.01: ('1000mg', '12/12h', ''),
            1000: ('1000mg', '8/8h', ''),
        }
    },
    'cip_oral': {
        'nome': 'Ciprofloxacino (Oral)',
        'dosing': {
            0.02: ('500mg', '24/24h', 'Administre após HD no dia da HD'),
            10: ('500mg', '24/24h', ''),
            1000: ('500mg', '12/12h', ''),
        }
    },
    'cip_iv': {
        'nome': 'Ciproflixacino (IV)',
        'dosing': {
            0.02: ('400mg', '24/24h', 'Administre após HD no dia da HD'),
            10: ('400mg', '24/24h', ''),
            50.01: ('400mg', '24/24h', ''),
            1000: ('400mg', '12/12h', ''),
        }
    },
    'cfu_oral': {
        'nome': 'Cefuroxima Axetil (Oral)',
        'dosing': {
            0.02: ('500mg', '48/48h', 'Administre dose extra de 500mg após HD'),
            10: ('500mg', '48/48h', ''),
            30.01: ('500mg', '24/24h', ''),
            1000: ('500mg', '12/12h', ''),
        }
    },
    'fos': {
        'nome': 'Fosfomicina (Oral)',
        'dosing': {
            0.02: ('3000mg', 'DU', 'Sem ajuste'),
            1000: ('2000mg', 'DU', 'Sem ajustes'),
        }
    },
    'lev_oral': {
        'nome': 'Levofloxacino (IV/Oral)',
        'dosing': {
            0.02: ('500mg', '48/48h', 'Primeira dose 750mg'),
            20: ('500mg', '48/48h', 'Primeira dose 750mg'),
            49.01: ('750mg', '48/48h', ''),
            1000: ('750mg', '24/24h', ''),
        }
    },
    'Te1': {
        'nome': 'Teicoplanina (PNM, IPPM, ITU complicada)',
        'dosing': {
            0.02: ('6mg/kg', '72/72h', 'Não é removida pela HD'),
            30: ('6mg/kg', '72/72h', 'Alvo: >15mcg/ml'),
            80.01: ('6mg/kg', '48/48h', 'Alvo: >15mcg/ml'),
            1000: ('6mg/kg', '24/24h', 'Alvo: >15mcg/ml'),
        }
    },
    'Te2': {
        'nome': 'Teicoplanina (Osteoarticular, Endocardite-EI)',
        'dosing': {
            0.02: ('12mg/kg', '72/72h', 'Não é removida pela HD'),
            30: ('12mg/kg', '72/72h', 'Alvo: >20mcg/ml (EI >30mcg/ml)'),
            80.01: ('12mg/kg', '48/48h', 'Alvo: >20mcg/ml (EI >30mcg/ml)'),
            1000: ('12mg/kg', '24/24h', 'Alvo: >20mcg/ml (EI >30mcg/ml)'),
        }
    },
    'pol': {
        'nome': 'Polimixina B',
        'dosing': {
            0.02: ('1.5mg/kg', '12/12h', 'Inicial 2.5mg/kg, (1mg = 10000 UI)'),
            1000: ('1.5mg/kg', '12/12h', 'Inicial 2.5mg/kg, (1mg = 10000 UI)'),
        }
    },
}

lista_atbs = [key for key in doses_dos_atbs.keys()]
