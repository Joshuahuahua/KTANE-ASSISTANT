def wires(bomb_data):
    
    wire_list = input('Please input wires, separated with a ",": ').split(", ")
    
    if len(wire_list) == 3:
        if 'red' not in wire_list:
            print (2)
        elif 'white' == wire_list[-1]:
            print (3)
        elif wire_list.count('blue') > 1:
            print(len(wire_list) - wire_list[::-1].index('blue'))
        else:
            print(3)
    
    if len(wire_list) == 4:
        if wire_list.count('red') > 1 and bomb_data['serial_odd']:
            print(len(wire_list) - wire_list[::-1].index('red'))
        elif 'red' not in wire_list and wire_list[-1] == 'yellow':
            print(1)
        elif wire_list.count('blue') == 1:
            print(1)
        elif wire_list.count('yellow') > 1:
            print(4)
        else:
            print(2)
    
    if len(wire_list) == 5:
        if wire_list[-1] == 'black' and bomb_data['serial_odd']:
            print(4)
        elif wire_list.count('red') == 1 and wire_list.count('yellow') > 1:
            print(1)
        elif 'black' not in wire_list:
            print(2)
        else:
            print(1)
    
    if len(wire_list) == 6:
        if 'yellow' not in wire_list and bomb_data['serial_odd']:
            print(3)
        elif wire_list.count('yellow') == 1 and wire_list.count('white') > 1:
            print(4)
        elif 'red' not in wire_list:
            print(6)
        else:
            print(4)