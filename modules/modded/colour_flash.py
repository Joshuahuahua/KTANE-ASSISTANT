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


    word_input = ['magenta', 'green', 'blue', 'yellow', 'yellow', 'yellow', 'yellow', 'red']
    colour_input = ['magenta', 'magenta', 'magenta', 'blue', 'magenta', 'magenta', 'yellow', 'yellow']

    result = colour_flash_answer(word_input, colour_input)
    print('Press', result[0].upper(), 'on word', result[1]+1)
    
    
    
def colour_flash_answer(word_input, colour_input):
    if colour_input[-1] == 'red':
        green_count = 0
        if word_input.count('green') > 2:
            for i in range(0,len(word_input)):
                if word_input[i] == 'green' or colour_input[i] == 'green':
                    green_count+=1
                    if green_count == 3:
                        return ['yes', i]
        elif word_input.count('blue') == 1:
            return ['no', word_input.index('magenta')]
        else:
            word_input.reverse()
            colour_input.reverse()
            for i in range(0,len(word_input)):
                if word_input[i] == 'white' or colour_input[i] == 'white':
                    return ['yes', len(word_input)-i-1]
                
    elif colour_input[-1] == 'yellow':
        for i in range(0,len(word_input)):
            if word_input[i] == 'blue' and colour_input[i] == 'green':
                for i in range(0,len(word_input)):
                    if word_input[i] == 'green' or colour_input[i] == 'green':
                        return ['yes', i]
        for i in range(0,len(word_input)):
            if word_input[i] == 'white' and (colour_input[i] == 'white' or colour_input[i] == 'red'):
                dif_count = 0
                for i in range(0,len(word_input)):
                    if word_input[i] != colour_input[i]:
                        dif_count+=1
                    if dif_count == 2:
                        return ['yes', i]
        magenta_count = 0
        for i in range(0,len(word_input)):
            if word_input[i] == 'magenta' or colour_input[i] == 'magenta':
                magenta_count+=1
        return ['no', magenta_count-1] # -1 because its +1 at the top

    elif colour_input[-1] == 'green':
        for i in range(0,len(word_input)):
            if i != 0:
                if word_input[i-1] == word_input[i] and colour_input[i-1] != colour_input[i] :
                     return 5-1 # -1 because its +1 at the top
        for i in range(0,len(word_input)):
            if word_input.count('magenta') > 2:
                for i in range(0,len(word_input)):
                    if word_input[i] == 'yellow' or colour_input[i] == 'yellow':
                        return ['no', i]
        for i in range(0,len(word_input)):
            if word_input[i] == colour_input[i]:
                return ['yes', i]
        
    elif colour_input[-1] == 'blue':
        dif_count = 0
        for i in range(0,len(word_input)):
            if word_input[i] != colour_input[i]:
                dif_count+=1
            if dif_count == 1:
                pos = i
            if dif_count > 2:
                return ['yes', pos]
        for i in range(0,len(word_input)):
            if (word_input[i] == 'red' and colour_input[i] == 'yellow') or (word_input[i] == 'yellow' and colour_input[i] == 'white'):
                if word_input[i] == 'white' and colour_input[i] == 'red':
                    return ['no', i]
        for i in range(0,len(word_input)):
            word_input.reverse()
            colour_input.reverse()
            for i in range(0,len(word_input)):
                if word_input[i] == 'green' or colour_input[i] == 'green':
                    return ['yes', len(word_input)-i-1]

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