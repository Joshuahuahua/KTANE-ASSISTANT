def simple_wires(bomb_data):
    
    wire_list = input('Please input wires, separated with a ",": ').lower().replace(', ', ',').split(',')
    
    if len(wire_list) == 3:
        if 'red' not in wire_list:
            print('Cut the second wire!')
        elif 'white' == wire_list[-1]:
            print('Cut the last wire!')
        elif wire_list.count('blue') > 1:
            print('Cut wire', len(wire_list) - wire_list[::-1].index('blue'))
        else:
            print('Cut the last wire!')
    
    elif len(wire_list) == 4:
        if wire_list.count('red') > 1 and bomb_data['serial_odd']:
            print('Cut wire', len(wire_list) - wire_list[::-1].index('red'))
        elif 'red' not in wire_list and wire_list[-1] == 'yellow':
            print('Cut the first wire!')
        elif wire_list.count('blue') == 1:
            print('Cut the first wire!')
        elif wire_list.count('yellow') > 1:
            print('Cut the last wire!')
        else:
            print('Cut the second wire!')
    
    elif len(wire_list) == 5:
        if wire_list[-1] == 'black' and bomb_data['serial_odd']:
            print('Cut the fourth wire!')
        elif wire_list.count('red') == 1 and wire_list.count('yellow') > 1:
            print('Cut the first wire!')
        elif 'black' not in wire_list:
            print('Cut the second wire!')
        else:
            print('Cut the first wire!')
    
    elif len(wire_list) == 6:
        if 'yellow' not in wire_list and bomb_data['serial_odd']:
            print('Cut the third wire!')
        elif wire_list.count('yellow') == 1 and wire_list.count('white') > 1:
            print('Cut the fourth wire!')
        elif 'red' not in wire_list:
            print('Cut the last wire!')
        else:
            print('Cut the fourth wire!')

    else:
        print('---ERROR---')
        print('Expected at least 3 wires!')