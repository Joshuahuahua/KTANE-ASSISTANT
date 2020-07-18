def piano_keys(bomb_data):
    key_dic = [
        {'condition': '', 'symbols': ['flat'], 'required': 'Even', 'sequence': 'Bb Bb Bb Bb Gb Ab Bb Ab Bb'},
        {'condition': 'OR', 'symbols': ['common time', 'sharp'], 'required': 'H2', 'sequence': 'Eb Eb D D Eb Eb D Eb Eb D D Eb'},
        {'condition': 'AND', 'symbols': ['natural', 'fermata'], 'required': '', 'sequence': 'E F# F# F# E E E'},
        {'condition': 'OR', 'symbols': ['cut time', 'turn'], 'required': 'RCA', 'sequence': 'Bb A Bb F Eb Bb A Bb F Eb'},
        {'condition': '', 'symbols': ['clef'], 'required': 'SND', 'sequence': 'E E E C E G G'},
        {'condition': 'OR', 'symbols': ['mordent', 'fermata', 'common time'], 'required': 'B3', 'sequence': 'C# D E F C# D E F Bb A'},
        {'condition': 'AND', 'symbols': ['flat', 'sharp'], 'required': '', 'sequence': 'G G C G G C G C'},
        {'condition': 'OR', 'symbols': ['cut time', 'mordent'], 'required': 'S378', 'sequence': 'A E F G F E D D F A'},
        {'condition': 'OR', 'symbols': ['Natural', 'Turn', 'Clef'], 'required': '', 'sequence': 'G G G Eb Bb G Eb Bb G'},
        {'condition': 'NO', 'symbols': [''], 'required': '', 'sequence': 'B D A G A B D A'}]


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
            print('Sequence: ' + key['sequence'])
        else:
            print('---ERROR---\nNo sequence found!')

    


def furtherRequirements(required):
    return True if required == ''
    return True if required == 'Even' and bomb_data['serial_odd'] == False
    return True if required == 'H2' and (bomb_data['bat_AA']/2) + bomb_data['bat_B'] == required[1:]
    return True if required == 'RCA' and bomb_data['port_rca'] == True
    return True if required == 'SND' and 'SND' in bomb_data['indicator_LIT']
    return True if required == 'B3' and bomb_data['bat_total'] > 2
    return True if required == 'S378' and any(x in bomb_data['serial'] for x in ['3', '7', '8'])
    return False