#Coded by Matthew Alphonso
def round_keypad(input_symbol):
    symbols = [
        {'name': 'paddle', 'character': 'Ϙ', 'value': 1},
        {'name': 'a', 'character': 'Ѧ', 'value': 2},
        {'name': 'landa', 'character': 'ƛ', 'value': 3},
        {'name': 'lightning', 'character': 'Ϟ', 'value': 4},
        {'name': 'alien', 'character': 'Ѭ', 'value': 5},
        {'name': 'curly h', 'character': 'ϗ', 'value': 6},
        {'name': 'backwards c', 'character': 'Ͽ', 'value': 7},
        {'name': 'e', 'character': 'Ӭ', 'value': 8},
        {'name': 'squiggle', 'character': 'Ҩ', 'value': 9},
        {'name': 'white star', 'character': '☆', 'value': 10},
        {'name': '?', 'character': '¿', 'value': 11},
        {'name': 'copyright', 'character': '©', 'value': 12},
        {'name': 'butt', 'character': 'Ѽ', 'value': 13},
        {'name': 'x', 'character': 'Җ', 'value': 14},
        {'name': 'r', 'character': 'Ԇ', 'value': 15},
        {'name': 'six', 'character': 'Ϭ', 'value': 16},
        {'name': 'p', 'character': '¶', 'value': 17},
        {'name': 'b', 'character': 'Ѣ', 'value': 18},
        {'name': 'smiley face', 'character': 'ټ', 'value': 19},
        {'name': 'trident', 'character': 'ψ', 'value': 20},
        {'name': 'c', 'character': 'Ͼ', 'value': 21},
        {'name': 'alien 3', 'character': 'Ѯ', 'value': 22},
        {'name': 'black star', 'character': '★', 'value': 23},
        {'name': 'not equal', 'character': '҂', 'value': 24},
        {'name': 'ae', 'character': 'æ', 'value': 25},
        {'name': 'straight h', 'character': 'Ҋ', 'value': 26},
        {'name': 'omega', 'character': 'Ω', 'value': 27},
    ]

    column_list = [
        {'column': [1,2,3,4,5,6,7], 'total': 0},
        {'column': [8,1,7,9,10,6,11], 'total': 0},
        {'column': [12,13,9,14,15,3,10], 'total': 0},
        {'column': [16,17,18,5,14,11,19], 'total': 0},
        {'column': [20,19,18,21,17,22,23], 'total': 0},
        {'column': [16,8,24,25,20,26,27], 'total': 0}
    ]
   
    #input_symbol = input('\nwrite 8 symbols:').lower().replace(', ', ',').replace('6', 'six').split(',')
    input_symbol = input_symbol.lower().replace(', ', ',').replace('6', 'six').split(',')
    if len(input_symbol) != 8:
        print('--ERROR--\nExpected 8 items!')
        return
    
    #convert name into value
    for i, current_input in enumerate(input_symbol):
        for symbol in symbols:
            if current_input == symbol['name']:
                input_symbol[i] = symbol['value']
    try:
        sum(input_symbol)
    except:
        print('--ERROR--\nOne or more of those symbols don\'t exist.')
        return
    
    #find column that contains most symbols
    for i, current_column in enumerate(column_list, 1):
        for symbol in input_symbol:
            if symbol in current_column['column']:
                current_column['total']+=1
    
    #find column that contains most symbols
    print(column_list)
    max_symbol = -1
    total_symbol_list = []
    for i , x in enumerate(column_list):
        total_symbol_list.append(column_list[i]['total'])
        if column_list[i]['total'] >= max_symbol:
            max_symbol = column_list[i]['total']
            max_symbol_index = i
    
    #print order
    print('\n---Type---\n')
    for symbol in column_list[max_symbol_index]['column']:
        if symbol not in input_symbol:
            print(str(symbols[symbol-1]['name']))
    print('-----------')
    return
