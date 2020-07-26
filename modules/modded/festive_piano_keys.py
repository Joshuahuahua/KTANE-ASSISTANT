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
                    if furtherRequirements(key['required'], bomb_data):
                        print('Sequence: ' + key['sequence'])
                        return

        elif key['condition'] == 'AND':
            if key['symbols'][0] in symbols_input and key['symbols'][1] in symbols_input:
                if furtherRequirements(key['required'], bomb_data):
                    print('Sequence: ' + key['sequence'])
                    return
        elif key['condition'] == 'NO':
            num = list(int(x) for x in bomb_data['serial'] if x.isdigit())
            num.sort(reverse=True)
            print('Sequence: ' + key['sequence']*num[0]+1)
        else:
            print('---ERROR---\nNo sequence found!')

def furtherRequirements(required, bomb_data):
    if required == '':
        return True
    if required == 'SE>O' and len(list(x for x in bomb_data['serial'] if x.isdigit() and int(x) %2 == 0)) > len(list(x for x in bomb_data['serial'] if x.isdigit() and int(x) %2 != 0)):
        return True
    if required == 'SDUPE' and len(set(bomb_data['serial'])) != len(bomb_data['serial']):
        return True
    if required == 'DifPort<3' and sum([1 for x in [bomb_data['port_parallel'],bomb_data['port_dvi'],bomb_data['port_ps2'],bomb_data['port_rj45'],bomb_data['port_serial'],bomb_data['port_rca']] if x > 0]) < 3:
        return True
    if required == 'IndVowel' and any(x in str(bomb_data['ind_LIT']) for x in ['A', 'E', 'I', 'O', 'U']):
        return True
    if required == 'AA>2' and bomb_data['bat_AA'] > 2:
        return True
    if required == 'S19' and any(x in bomb_data['serial'] for x in ['1', '9']):
        return True
    else:
        return False