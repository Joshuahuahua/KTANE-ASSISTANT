def morse(passed_param):
    morse_dic = [
        {'code': ['-...', '.'],           'word': 'BEATS', 'frequency': '3.600MHz'},
        {'code': ['-...', '..'],          'word': 'BISTRO', 'frequency': '3.552MHz'},
        {'code': ['-...', '---', '--'],   'word': 'BOMBS', 'frequency': '3.565MHz'},
        {'code': ['-...', '---', '-..-'], 'word': 'BOXES', 'frequency': '3.535MHz'},
        {'code': ['-...', '-.-', '.'],    'word': 'BREAK', 'frequency': '3.572MHz'},
        {'code': ['-...', '-.-', '..'],   'word': 'BRICK', 'frequency': '3.575MHz'},
        {'code': ['..-.'],                'word': 'FLICK', 'frequency': '3.555MHz'},
        {'code': ['....'],                'word': 'HALLS', 'frequency': '3.515MHz'},
        {'code': ['.-..'],                'word': 'LEAKS', 'frequency': '3.542MHz'},
        {'code': ['...', '....'],         'word': 'SHELL', 'frequency': '3.505MHz'},
        {'code': ['...', '.-..'],         'word': 'SLICK', 'frequency': '3.522MHz'},
        {'code': ['...', '-', '.'],       'word': 'STEAK', 'frequency': '3.582MHz'},
        {'code': ['...', '-', '..'],      'word': 'STING', 'frequency': '3.592MHz'},
        {'code': ['...', '-', '.-.'],     'word': 'STROBE', 'frequency': '3.545MHz'},
        {'code': ['-'],                   'word': 'TRICK', 'frequency': '3.532MHz'},
        {'code': ['...-'],                'word': 'VECTOR', 'frequency': '3.595MHz'}
    ]
    morse_input = []
    while True:
        #morse_input.append(input('Separate letters with a space, Use . and -\nInput morse code: '))
        morse_input.append(passed_param)
        if morse_input[-1] == 'r':
            morse_input = []
            print('---Reset---')
        elif morse_input[-1] == 'x':
            return
        for word in morse_dic:
            if word['code'] == morse_input:
                print('The frequency is: ' + str(word['frequency']))
                return
        if len(morse_input) == 3:
            print('---ERROR---\nFrequency not found!')
            break