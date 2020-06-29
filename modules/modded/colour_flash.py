def colour_flash(bomb_data):
    colour_dic = ['red', 'yellow', 'green', 'blue', 'magenta', 'white']
    
    word_input = input('Usage <word1, word2, etc>: ').lower().replace(', ', ',').split(',')
    colour_input = input('Usage <colour1>, colour2, etc>: ').lower().replace(', ', ',').split(',')
    
    convert(word_input, colour_dic)
    convert(colour_input, colour_dic)

    if len(word_input) != 8 or len(colour_input) != 8:
        print('\n--ERROR--\nExpected 8 items!')
        return


    if colour_input[-1] == 'red':
        pass
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
    


colour_flash('w')