def cruel_piano_keys(bomb_data):
    key_dic = [
        {'condition': '', 'symbols': ['break'], 'required': 'SE>O', 'lookup': '', 'transformation': ['I', 'R']},
        {'condition': 'OR', 'symbols': ['s', 'note'], 'required': 'SDUPE', 'lookup': '', 'transformation': ['T', 'minsRem']},
        {'condition': 'AND', 'symbols': ['mordent', 'pedal'], 'required': '', 'lookup': '', 'transformation': ['I']},
        {'condition': 'OR', 'symbols': ['up bow', 'down bow'], 'required': 'DifPort<3', 'lookup': '', 'transformation': ['R']},
        {'condition': '', 'symbols': ['accent'], 'required': 'IndVowel', 'lookup': '', 'transformation': ['R', 'T', 3]},
        {'condition': 'OR', 'symbols': ['rest', 'note'], 'required': 'AA>2', 'lookup': '', 'transformation': 'T', bomb_data['port_total']},
        {'condition': 'AND', 'symbols': ['semibreve', 'breve'], 'required': '', 'lookup': '', 'transformation': 'I'},
        {'condition': 'OR', 'symbols': ['dim', 'accent', 'up bow'], 'required': 'S19', 'lookup': '', 'transformation': 'R'},
        {'condition': 'OR', 'symbols': ['s', 'clef', 'break'], 'required': '', 'lookup': '', 'transformation': 'P'},
        {'condition': 'NO'}]

    sequence_dic = [
        ['F', 'D', 'F#', 'G#', 'C', 'B', 'A#', 'C#', 'G', 'E', 'D#', 'A'],
        ['A#', 'A', 'C', 'E', 'C#', 'D', 'D#', 'G', 'B', 'F#', 'G#', 'F'],
        ['F#', 'B', 'A', 'G', '#D', 'C', 'G', 'C#', 'F', 'D#', 'E', 'A#'],
        ['E', 'D#', 'D', 'F#', 'F', 'A#', 'G#', 'C#', 'C', 'B', 'G', 'A'],
        ['D', 'E', 'A', 'A#', 'C', 'B', 'C#', 'G#', 'F', 'F#', 'D#', 'G'],
        ['C', 'D#', 'F#', 'D', 'F', 'C#', 'B', 'A', 'G', 'A#', 'E', 'G#'],
        ['G#', 'C', 'A#', 'C#', 'E', 'G', 'B', 'D#', 'A', 'D', 'F', 'F#'],
        ['E', 'A', 'C#', 'B', 'G', 'G#', 'A#', 'D#', 'F#', 'F', 'C', 'D'],
        ['G#', 'D#', 'D', 'E', 'A#', 'C#', 'F#', 'G', 'F', 'A', 'C', 'B'],
        ['D#', 'G#', 'C', 'B', 'D', 'C#', 'F#', 'A#', 'F', 'G', 'A', 'E']
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
    
    
    symbols_input = input('Usage <symbol1, symbol2, symbol3>: ').lower().replace(', ', ',').split(',')

    for key in key_dic:
        if key['condition'] != 'AND':
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
            print('Sequence: ' + key['sequence']*num[0]+1))
        else:
            print('---ERROR---\nNo sequence found!')

def furtherRequirements(required):
    if required == '':
        return True
    elif required == 'SE>O' and len(list(x for x in bomb_data['serial'] if x.isdigit() and int(x) %2 == 0)) > len(list(x for x in bomb_data['serial'] if x.isdigit() and int(x) %2 != 0)):
        return True
    elif required == 'SDUPE' and len(set(bomb_data['serial'])) != len(bomb_data['serial']):
        return True
    elif required == 'DifPort<3' and [bomb_data['port_parallel'], bomb_data['port_dvi'], bomb_data['port_ps2'], bomb_data['port_rj45'], bomb_data['port_serial'], bomb_data['port_rca']].count(True) < 3:
        return True
    elif required == 'IndVowel' and any(x in str(bomb_data['ind_LIT']) for x in ['A', 'E', 'I', 'O', 'U']):
        return True
    elif required == 'AA>2' and bomb_data['bat_AA'] > 2:
        return True
    elif required == 'S19' and any(x in bomb_data['serial'] for x in ['1', '9']):
        return True
    else:
        return False



bomb_data = {
    'bat_AA': 2,
    'bat_B': 0,
    'bat_total': 2,
    'ind_LIT': ['TRN', 'BOB'],
    'ind_UNLIT': ['CAR'],
    'serial': '1T5FI5',
    'serial_odd': False,
    'serial_vowel': True,
    'port_parallel': False,
    'port_dvi': False,
    'port_ps2': False,
    'port_rj45': False,
    'port_serial': False,
    'port_rca': False,
    'modules_total': 101,
    'modules_solved': 0,
}

festive_piano_keys(bomb_data)