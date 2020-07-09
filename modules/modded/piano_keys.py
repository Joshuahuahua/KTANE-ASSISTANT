def piano_keys(bomb_data):
    key_dic = [
        {'condition': '', 'symbols': ['Flat'], 'required': 'Even', 'sequence': 'Bb Bb Bb Bb Gb Ab Bb Ab Bb'},
        {'condition': 'OR', 'symbols': ['Common Time', 'Sharp'], 'required': 'H2', 'sequence': 'Eb Eb D D Eb Eb D Eb Eb D D Eb'},
        {'condition': 'AND', 'symbols': ['Natural', 'Fermata'], 'required': '', 'sequence': 'E F# F# F# E E E'},
        {'condition': 'OR', 'symbols': ['Cut Time', 'Turn'], 'required': 'RCA', 'sequence': 'Bb A Bb F Eb Bb A Bb F Eb'},
        {'condition': '', 'symbols': ['Clef'], 'required': 'SND', 'sequence': 'E E E C E G G'},
        {'condition': 'OR', 'symbols': ['Trill', 'Fermata', 'Common Time'], 'required': 'B3', 'sequence': 'C# D E F C# D E F Bb A'},
        {'condition': 'AND', 'symbols': ['Flat', 'Sharp'], 'required': '', 'sequence': 'G G C G G C G C'},
        {'condition': 'OR', 'symbols': ['Cut Time', 'Trill'], 'required': 'S378', 'sequence': 'A E F G F E D D F A'},
        {'condition': 'OR', 'symbols': ['Natural', 'Turn', 'Clef'], 'required': '', 'sequence': 'G G G Eb Bb G Eb Bb G'},
        {'condition': 'NO', 'symbols': [''], 'required': '', 'sequence': 'B D A G A B D A'}
    ]



    symbols_input = input('Usage <symbol1, symbol2, symbol3>: ').capitalize().replace(', ', ',').split(',')


    for i, key in enumerate(key_dic):
        if key['condition'] != 'AND':
            for symbol in key['symbols']:
                if symbol in symbols_input:
                    if furtherRequirements(key['required'] == True):
                        print('Sequence: ' + key['sequence'])

'''
	If (Pianokeys[A_Index].Condition = 'AND') {
		SymbolArray := StrSplit(Pianokeys[A_Index].Symbols, ',', A_Space)
		msgbox % '1: ' SymbolArray[1] ' 2: ' SymbolArray[2] 
		If InStr(pkSymbols, SymbolArray[1]) AND InStr(pkSymbols, SymbolArray[2]) {
			msgbox yep`, that worked
			msgbox % Pianokeys[A_Index].Required
			test := FurtherRequirements(Pianokeys[A_Index].Required)
			msgbox % test
			If (FurtherRequirements(Pianokeys[A_Index].Required) = True) {
				String := Pianokeys[Key].Sequence
				MsgBox, 64, %Title%, Input the sequence: `n %String%
				ExitApp
			}
		}
	}
}
ExitApp



'''

def furtherRequirements(required):
	if required == ''):
		return True
	elif required == 'Even') {
		if bomb_data['odd'] == False:
            return True
        else:
            return False
	else:
		return False





bomb_data = {
    'bat_AA': 0,
    'bat_B': 0,
    'bat_total': 0,
    'ind_LIT': [],
    'ind_UNLIT': [],
    'serial': S2A2N2,
    'serial_odd': False,
    'serial_vowel': False,
    'port_parallel': False,
    'port_dvi': False,
    'port_ps2': False,
    'port_rj45': False,
    'port_serial': False,
    'port_rca': False,
    'modules_total': 101,
    'modules_solved': 0,
    }
piano_keys(bomb_data)
