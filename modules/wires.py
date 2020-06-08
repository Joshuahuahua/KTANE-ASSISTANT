def wires(bomb_data):
    '''
    colors = ['red', 'white', 'blue', 'yellow', 'black']
    color_dict = {}

    for color in colors:
        color_dict[color] = int(input('How many ' + color + ' wires? > '))
    
    wires = red + white + blue + yellow + black
    if wires == 3:
        found = False
        if color_dict['red'] == 0:
            print('Cut the second wire')
            found = True
        if not found and white > 0:
            if input('Is the white wire the last wire? (Y/N) > ').lower() == 'y':
                print('Cut the last wire')
                found = True
        if not found and blue > 1:
            print('Cut the last blue wire')
            found = True
        if not found:
            print('Cut the last wire')
            found = True
    if wires == 4:
        pass
    if wires == 5:
        pass
    if wires == 6:
        pass
    '''
    wire_list = input('Please input wires, separated with a ",": ').split(", ")
    print(wire_list)
    print(len(wire_list))
    print(wire_list.count('red'))
    print(bomb_data['test'])

    '''


    '''