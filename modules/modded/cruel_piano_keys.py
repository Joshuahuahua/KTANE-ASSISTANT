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
        ['F', 'D', 'F#', 'G#', 'C', 'B', 'A#', 'C#', 'G', 'E', 'D#', 'A'],
        ['A#', 'A', 'C', 'E', 'C#', 'D', 'D#', 'G', 'B', 'F#', 'G#', 'F'],
        ['F#', 'B', 'A', 'G#', 'D', 'C', 'G', 'C#', 'F', 'D#', 'E', 'A#'],
        ['E', 'D#', 'D', 'F#', 'F', 'A#', 'G#', 'C#', 'C', 'B', 'G', 'A'],
        ['D', 'E', 'A', 'A#', 'C', 'B', 'C#', 'G#', 'F', 'F#', 'D#', 'G'],
        ['C', 'D#', 'F#', 'D', 'F', 'C#', 'B', 'A', 'G', 'A#', 'E', 'G#'],
        ['G#', 'C', 'A#', 'C#', 'E', 'G', 'B', 'D#', 'A', 'D', 'F', 'F#'],
        ['E', 'A', 'C#', 'B', 'G', 'G#', 'A#', 'D#', 'F#', 'F', 'C', 'D'],
        ['G#', 'D#', 'D', 'E', 'A#', 'C#', 'F#', 'G', 'F', 'A', 'C', 'B'],
        ['D#', 'G#', 'C', 'B', 'D', 'C#', 'F#', 'A#', 'F', 'G', 'A', 'E']
    ]

    global translate_dic
    translate_dic = [
        {'value': 0, 'note': 'C'},
        {'value': 1, 'note': 'C#'},
        {'value': 2, 'note': 'D'},
        {'value': 3, 'note': 'D#'},
        {'value': 4, 'note': 'E'},
        {'value': 5, 'note': 'F'},
        {'value': 6, 'note': 'F#'},
        {'value': 7, 'note': 'G'},
        {'value': 8, 'note': 'G#'},
        {'value': 9, 'note': 'A'},
        {'value': 10, 'note': 'A#'},
        {'value': 11, 'note': 'B'}
    ]
    

    symbols_input = input('Usage <symbol1, symbol2...symbol4>: ').lower().replace(', ', ',').split(',')

    for key in key_dic:
        if key['condition'] == 'OR':
            for symbol in key['symbols']:
                if symbol in symbols_input:
                    if furtherRequirements(key['required'], bomb_data):
                        sequence = sequence_dic[key['lookup']]
                        convert(sequence, 'value')
                        transform(key['transformation'], sequence)
                        convert(sequence, 'note')
                        print('Sequence: ' + ', '.join(sequence))
                        return [True]

        elif key['condition'] == 'AND':
            if key['symbols'][0] in symbols_input and key['symbols'][1] in symbols_input:
                if furtherRequirements(key['required'], bomb_data):
                    print('Sequence: ' + transform(key['transformation'], key['sequence']))
                    return [True]
        else:
            print('return false')
            return [False, symbols_input]



def furtherRequirements(required, bomb_data):
    #return True
    if required == '':
        return True
    elif required == '2+ind' and len(bomb_data['ind_LIT'])+len(bomb_data['ind_UNLIT']) > 1:
        return True
    elif required == 'empty plate' and bomb_data['port_plate_empty'] > 0:
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
    for i, method in enumerate(mode):
        if method == 'R':
            sequence.reverse()
        elif method == 'T':
            sequence = list((x+mode[i+1]) % 12 for x in sequence)
        elif method == 'I':
            newList = sequence
            for i in range(0,len(sequence)-1):
                tempList = []
                diff = sequence[i]-sequence[i+1]
                for item in newList[:i+1]:
                    tempList.append(item)
                for x in range(0, len(newList[i+1:])):
                    tempList.append(newList[i:][x]+diff)
                newList = tempList
            sequence = list(x % 12 for x in tempList)
    return sequence

def convert(sequence, mode):
    for i, current_input in enumerate(sequence):
        for note in translate_dic:
            if mode == 'note':
                if current_input == note['value']:
                    sequence[i] = note['note']
            else:
                if current_input == note['note']:
                    sequence[i] = note['value']
    return sequence

'''
bomb_data = {
    'bat_AA': 0,
    'bat_B': 1,
    'bat_total': 1,
    'ind_LIT': ['SIG', 'SNG'],
    'ind_UNLIT': [],
    'serial': 'Z25BB1',
    'serial_odd': 1,
    'serial_vowel': 0,
    'port_parallel': 0,
    'port_dvi': 0,
    'port_ps2': 1,
    'port_rj45': 2,
    'port_serial': 0,
    'port_rca': 2,
    'port_total': 5,
    'port_plate': 2,
    'port_plate_empty': 0,
    'strikes': 0,
    'modules_total': 4,
    'modules_solved': 0,
}

cruel_piano_keys(bomb_data)
'''