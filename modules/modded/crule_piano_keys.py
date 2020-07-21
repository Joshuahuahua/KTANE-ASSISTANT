def cruel_piano_keys(bomb_data):
    key_dic = [
        {'condition': 'AND', 'symbols': ['breve', 'turn'], 'required': '2+ind', 'lookup': list(x for x in bomb_data['serial'] if x.isdigit())[0], 'transformation': ['I', 'R']},
        {'condition': 'OR', 'symbols': ['sharp', 'double sharp'], 'required': 'empty plate', 'lookup': wrap((bomb_data['bat_AA']/2)+bomb_data['bat_B'], 0, 9), 'transformation': ['T', 'minsRem']},
        {'condition': 'OR', 'symbols': ['fermata', 'down bow'], 'required': '2+samePort', 'lookup': int(str(bomb_data['modules_solved'])[-1]), 'transformation': ['I']},
        {'condition': 'AND', 'symbols': ['clef', '8 rest'], 'required': '2+plate', 'lookup': wrap(9-len(bomb_data['ind_UNLIT']), 0, 9), 'transformation': ['R']},
        {'condition': 'OR', 'symbols': ['cut time', 'common time'], 'required': 'Svowel', 'lookup': int(str(bomb_data['strikes'])[-1]), 'transformation': ['R', 'T', 3]},
        {'condition': 'OR', 'symbols': ['natural', 'mordent'], 'required': 'batEven', 'lookup': 7 if bomb_data['port_dvi'] > 0 else 3, 'transformation': ['T', bomb_data['port_total']]},
        {'condition': 'OR', 'symbols': ['flat', '4 rest'], 'required': 'indNoVowel', 'lookup': 8, 'transformation': ['I']},
        {'condition': 'OR', 'symbols': ['down bow', '8 rest'], 'required': '>2Port', 'lookup': 4, 'transformation': ['R']},
        {'condition': 'OR', 'symbols': ['breve', 'double sharp'], 'required': '', 'lookup': 5, 'transformation': ['P']},
        {'condition': 'NO'}
    ]

    sequence_dic = [
        [6, 3, 7, 9, 1, 12, 11, 2, 8, 5, 4, 10]
        [11, 10, 1, 5, 2, 3, 4, 8, 12, 7, 9, 6],
        [7, 12, 10, 9, 3, 1, 8, 2, 6, 4, 5, 11],
        [5, 4, 3, 7, 6, 11, 9, 2, 1, 12, 8, 10],
        [3, 5, 10, 11, 1, 12, 2, 9, 6, 7, 4, 8],
        [1, 4, 7, 3, 6, 2, 12, 10, 8, 11, 5, 9],
        [9, 1, 11, 2, 5, 8, 12, 4, 10, 3, 6, 7],
        [5, 10, 2, 12, 8, 9, 11, 4, 7, 6, 1, 3],
        [9, 4, 3, 5, 11, 2, 7, 8, 6, 10, 1, 12],
        [4, 9, 1, 12, 3, 2, 7, 11, 6, 8, 10, 5]
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
                        print('Sequence: ' + key['sequence'])
                        return

        elif key['condition'] == 'AND':
            if key['symbols'][0] in symbols_input and key['symbols'][1] in symbols_input:
                if furtherRequirements(key['required']):
                    print('Sequence: ' + key['sequence'])
                    return
        elif key['condition'] == 'NO':
            num = list(int(x) for x in bomb_data['serial'] if x.isdigit())
            num.sort(reverse=True)
            print('Sequence: ' + key['sequence']*num[0]+1)
        else:
            print('---ERROR---\nNo sequence found!')

def furtherRequirements(required):
    if required == '':
        return True
    elif required == '2+ind' and len(bomb_data['ind_LIT'])+len(bomb_data['ind_UNLIT']) > 1:
        return True
    elif required == 'empty plate' and input('Is there an empty port plate? (Y/N): ').lower == 'y'):
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
    return

def wrap(x, xmin, xmax):
    while not xmax > x > xmin:
        x = x+xmax if x < xmin else x-xmax
    return x


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
    'modules_total': 101,
    'modules_solved': 0,
}

cruel_piano_keys(bomb_data)