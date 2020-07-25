def cruel_piano_keys(bomb_data):
    key_dic = [
        {'condition': 'AND', 'symbols': ['breve', 'turn'], 'required': '2+ind', 'lookup': list(x for x in bomb_data['serial'] if x.isdigit())[0], 'transformation': ['I', 'R']},
        {'condition': 'OR', 'symbols': ['sharp', 'double sharp'], 'required': 'empty plate', 'lookup': ((bomb_data['bat_AA']/2)+bomb_data['bat_B']) % 10, 'transformation': ['T', 'minsRem']},
        {'condition': 'OR', 'symbols': ['fermata', 'down bow'], 'required': '2+samePort', 'lookup': int(str(bomb_data['modules_solved'])[-1]), 'transformation': ['I']},
        {'condition': 'AND', 'symbols': ['clef', '8 rest'], 'required': '2+plate', 'lookup': (9-len(bomb_data['ind_UNLIT'])) % 10, 'transformation': ['R']},
        {'condition': 'OR', 'symbols': ['cut time', 'common time'], 'required': 'Svowel', 'lookup': int(str(bomb_data['strikes'])[-1]), 'transformation': ['R', 'T', -3]},
        {'condition': 'OR', 'symbols': ['natural', 'mordent'], 'required': 'batEven', 'lookup': 7 if bomb_data['port_dvi'] > 0 else 3, 'transformation': ['T', bomb_data['port_total']]},
        {'condition': 'OR', 'symbols': ['flat', '4 rest'], 'required': 'indNoVowel', 'lookup': 8, 'transformation': ['I']},
        {'condition': 'OR', 'symbols': ['down bow', '8 rest'], 'required': '>2Port', 'lookup': 4, 'transformation': ['R']},
        {'condition': 'OR', 'symbols': ['breve', 'double sharp'], 'required': '', 'lookup': 5, 'transformation': ['P']},
        {'condition': 'NO'}
    ]

    sequence_dic = [
        [5, 2, 6, 8, 0, 11, 10, 1, 7, 4, 3, 9],
        [10, 9, 0, 4, 1, 2, 3, 7, 11, 6, 8, 5],
        [6, 11, 9, 8, 2, 0, 7, 1, 5, 3, 4, 10],
        [4, 3, 2, 6, 5, 10, 8, 1, 0, 11, 7, 9],
        [2, 4, 9, 10, 0, 11, 1, 8, 5, 6, 3, 7],
        [0, 3, 6, 2, 5, 1, 11, 9, 7, 10, 4, 8],
        [8, 0, 10, 1, 4, 7, 11, 3, 9, 2, 5, 6],
        [4, 9, 1, 11, 7, 8, 10, 3, 6, 5, 0, 2],
        [8, 3, 2, 4, 10, 1, 6, 7, 5, 9, 0, 11],
        [3, 8, 0, 11, 2, 1, 6, 10, 5, 7, 9, 4]
    ]


    translate_dic = [
        {'value': 1, 'note': 'C'},
        {'value': 2, 'note': 'C#'},
        {'value': 3, 'note': 'D'},
        {'value': 4, 'note': 'D#'},
        {'value': 5, 'note': 'E'},
        {'value': 6, 'note': 'F'},
        {'value': 7, 'note': 'F#'},
        {'value': 8, 'note': 'G'},
        {'value': 9, 'note': 'G#'},
        {'value': 10, 'note': 'A'},
        {'value': 11, 'note': 'A#'},
        {'value': 12, 'note': 'B'}
    ]
    

    symbols_input = input('Usage <symbol1, symbol2...symbol4>: ').lower().replace(', ', ',').split(',')

    for key in key_dic:
        if key['condition'] == 'OR':
            for symbol in key['symbols']:
                if symbol in symbols_input:
                    if furtherRequirements(key['required']):
                        print('Sequence: ' + transform(key['transformation'], key['sequence']))
                        return

        elif key['condition'] == 'AND':
            if key['symbols'][0] in symbols_input and key['symbols'][1] in symbols_input:
                if furtherRequirements(key['required']):
                    print('Sequence: ' + transform(key['transformation'], key['sequence']))
                    return
        else:
            return False



def furtherRequirements(required):
    return True
    if required == '':
        return True
    elif required == '2+ind' and len(bomb_data['ind_LIT'])+len(bomb_data['ind_UNLIT']) > 1:
        return True
    elif required == 'empty plate' and input('Is there an empty port plate? (Y/N): ').lower == 'y':
        return True
    elif required == '2+samePort' and sum([1 for x in [bomb_data['port_parallel'],bomb_data['port_dvi'],bomb_data['port_ps2'],bomb_data['port_rj45'],bomb_data['port_serial'],bomb_data['port_rca']] if x > 0]) < 3:
        return True
    elif required == '2+plate' and bomb_data['port_plate'] > 1:
        return True
    elif required == 'Svowel' and bomb_data['serial_vowel']:
        return True
    elif required == 'batEven' and bomb_data['bat_total'] %2 == 0:
        return True
    elif required == 'indNoVowel' and not any(x in str(bomb_data['ind_LIT']+bomb_data['ind_UNLIT']) for x in ['A', 'E', 'I', 'O', 'U']):
        return True
    elif required == '>2Port' and bomb_data['port_total'] < 2:
        return True
    else:
        return False


def transform(mode, sequence):
    for method in mode:
        if method = 'R':
            sequence = sequence.reverse()



bomb_data = {
    'bat_AA': 2,
    'bat_B': 0,
    'bat_total': 2,
    'ind_LIT': ['TRN', 'BOB'],
    'ind_UNLIT': ['CAR'],
    'serial': '1T5FI5',
    'serial_odd': 0,
    'serial_vowel': 0,
    'port_parallel': 0,
    'port_dvi': 0,
    'port_ps2': 0,
    'port_rj45': 0,
    'port_serial': 0,
    'port_rca': 0,
    'port_total': 0,
    'port_plate': 0,
    'strikes': 0,
    'modules_total': 101,
    'modules_solved': 0,
}

cruel_piano_keys(bomb_data)