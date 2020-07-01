def colour_flash(bomb_data):
    colour_dic = ['red', 'yellow', 'green', 'blue', 'magenta', 'white']
    '''
    word_input = input('Usage <word1, word2, etc>: ').lower().replace(', ', ',').split(',')
    colour_input = input('Usage <colour1>, colour2, etc>: ').lower().replace(', ', ',').split(',')

    convert(word_input, colour_dic)
    convert(colour_input, colour_dic)

    if len(word_input) != 8 or len(colour_input) != 8:
        print('\n--ERROR--\nExpected 8 items!')
        return
    '''


    word_input = ['red', 'white', 'magenta', 'magenta', 'blue', 'green', 'white', 'white']
    colour_input = ['white', 'magenta', 'blue', 'blue', 'green', 'yellow', 'magenta', 'red']

    print('Press word:', colour_flash_answer(word_input, colour_input))
    
    
    
    def colour_flash_answer(word_input, colour_input)
        if colour_input[-1] == 'red':
            green_count = 0
            for i, x in enumerate(word_input):
                if word_input[i] == 'green' or colour_input[i] == 'green':
                    green_count+=1
                    if green_count == 3:
                        return i
            if word_input.count('blue') == 1:
                


        elif colour_input[-1] == 'yellow':
            pass
        elif colour_input[-1] == 'green':
            pass
        elif colour_input[-1] == 'blue':
            pass
        elif colour_input[-1] == 'magenta':
            pass
        else:
            pass









def convert(input_raw, colour_dic):
    for i, input_sub in enumerate(input_raw):
        for colour in colour_dic:
            if input_sub[0] == colour[0]:
                input_raw[i] = colour
    


bomb_data = {
    'bat_AA': 0,
    'bat_B': 0,
    'bat_total': 0,
    'ind_LIT': [],
    'ind_UNLIT': [],
    'serial': 'AAAA',
    'serial_odd': 0,
    'serial_vowel': 0,
    'port_parallel': 0,
    'port_dvi': False,
    'port_ps2': False,
    'port_rj45': False,
    'port_serial': False,
    'port_rca': False,
    'modules_total': 101,
    'modules_solved': 0,
}
colour_flash(bomb_data)