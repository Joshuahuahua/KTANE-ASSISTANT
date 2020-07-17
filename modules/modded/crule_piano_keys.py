def festive_piano_keys(bomb_data):
    key_dic = [
        {'condition': '', 'symbols': ['break'], 'required': 'SE>O', 'sequence': 'Eb F Eb C Ab F Eb'},
        {'condition': 'OR', 'symbols': ['s', 'note'], 'required': 'SDUPE', 'sequence': 'C# B A F# G# A G# F#'},
        {'condition': 'AND', 'symbols': ['mordent', 'pedal'], 'required': '', 'sequence': 'G A G E G A G E'},
        {'condition': 'OR', 'symbols': ['up bow', 'down bow'], 'required': 'DifPort<3', 'sequence': 'Eb Eb Db Ab Eb Eb F Db'},
        {'condition': '', 'symbols': ['accent'], 'required': 'IndVowel', 'sequence': 'B A G Eb D A B A G'},
        {'condition': 'OR', 'symbols': ['rest', 'note'], 'required': 'AA>2', 'sequence': 'F# G A A D B A G E D'},
        {'condition': 'AND', 'symbols': ['semibreve', 'breve'], 'required': '', 'sequence': 'G E F G C B C D C B A G'},
        {'condition': 'OR', 'symbols': ['dim', 'accent', 'up bow'], 'required': 'S19', 'sequence': 'G G G G G G G Bb Eb F G'},
        {'condition': 'OR', 'symbols': ['s', 'clef', 'break'], 'required': '', 'sequence': 'D D D C# C# C# B C# B F#'},
        {'condition': 'NO', 'symbols': [''], 'required': '', 'sequence': 'Bb A Bb G '}]

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