def wires(bomb_data, wire_list):
    
    if len(wire_list) == 3:
        if 'red' not in wire_list:
            return str(2)
        elif 'white' == wire_list[-1]:
            return str (3)
        elif wire_list.count('blue') > 1:
            return str(len(wire_list) - wire_list[::-1].index('blue'))
        else:
            return str(3)
    
    if len(wire_list) == 4:
        if wire_list.count('red') > 1 and bomb_data['serial_odd']:
            return str(len(wire_list) - wire_list[::-1].index('red'))
        elif 'red' not in wire_list and wire_list[-1] == 'yellow':
            return str(1)
        elif wire_list.count('blue') == 1:
            return str(1)
        elif wire_list.count('yellow') > 1:
            return str(4)
        else:
            return str(2)
    
    if len(wire_list) == 5:
        if wire_list[-1] == 'black' and bomb_data['serial_odd']:
            return str(4)
        elif wire_list.count('red') == 1 and wire_list.count('yellow') > 1:
            return str(1)
        elif 'black' not in wire_list:
            return str(2)
        else:
            return str(1)
    
    if len(wire_list) == 6:
        if 'yellow' not in wire_list and bomb_data['serial_odd']:
            return str(3)
        elif wire_list.count('yellow') == 1 and wire_list.count('white') > 1:
            return str(4)
        elif 'red' not in wire_list:
            return str(6)
        else:
            return str(4)