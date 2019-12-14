doses_dos_atbs = {
    'asb': {
        'nome': 'Ampicilina-Sulbactam',
        'dosing': {
            0.02: (3000, 24, 'No dia da HD, administrar a dose após a HD'),
            10: (3000, 24, ''),
            50.01: (3000, 12, ''),
            1000: (3000, 6, ''),
        }
    },
    'amc_oral': {
        'nome': 'Amoxicilina-Clavulanato (Oral)',
        'dosing': {
            0.02: (500, 24, 'No dia da HD, administrar uma dose extra após a HD'),
            10: (500, 24, ''),
            50.01: (500, 12, ''),
            1000: (500, 8, ''),
        }
    },
    'amc_iv': {
        'nome': 'Amoxicilina-Clavulanato (IV)',
        'dosing': {
            0.02: (500, 24, 'No dia da HD, administrar uma dose extra após a HD'),
            10: (500, 24, ''),
            30.01: (500, 12, ''),
            1000: (500, 8, ''),
        }
    },
    'cfz': {
        'nome': 'Cefazolina',
        'dosing': {
            0.02: (2000, 24, 'No dia da HD, administrar dose extra de 1000mg após a HD'),
            10: (2000, 24, ''),
            50.01: (1000, 8, ''),
            1000: (2000, 8, ''),
        }
    },
    'cpm': {
        'nome': 'Cefepime',
        'dosing': {
            0.02: (1000, 24, 'No dia da HD, administrar a dose após a HD'),
            10: (1000, 24, ''),
            30: (2000, 24, ''),
            60.01: (2000, 12, ''),
            1000: (2000, 8, ''),
        }
    },
    'caz': {
        'nome': 'Ceftazidima',
        'dosing': {
            0.02: (2000, 48, 'No dia da HD, administrar dose extra de 1000mg após a HD'),
            10: (2000, 48, ''),
            50.01: (2000, 24, ''),
            1000: (2000, 8, ''),
        }
    },
    'atm': {
        'nome': 'Aztreonam',
        'dosing': {
            0.02: (2000, 24, 'No dia da HD, administrar a dose após a HD'),
            10: (2000, 24, ''),
            50.01: (1000, 8, ''),
            1000: (2000, 8, ''),
        }
    },
}

lista_atbs = [key for key in doses_dos_atbs.keys()]
