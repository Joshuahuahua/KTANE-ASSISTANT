def complex_wires(bomb_data):
    wire_always = ['1010', '0000', '0010']
    wire_even = ['1000', '0100', '1100', '1101']
    wire_parallel = ['1110', '0101', '0111']
    wire_batteries = ['0011', '1001', '1011']
    
    while True:
        wire = [0,0,0,0]
        perams = input('Usage <trait1, trait2...>: ').lower().replace(' ', '').split(',')
        if perams[0] == 'x':
            return
        if 'red' in perams:
            wire[0]+=1
        if 'blue' in perams:
            wire[1]+=1
        if 'star' in perams:
            wire[2]+=1
        if 'led' in perams:
            wire[3]+=1
        wire = str(''.join([str(i) for i in wire]))

        if wire in wire_always:
            print('Cut the wire!\n')
        elif not bomb_data['serial_odd'] and wire in wire_even:
            print('Cut the wire!\n')
        elif bomb_data['port_parallel'] and wire in wire_parallel:
            print('Cut the wire!\n')
        elif bomb_data['bat_total'] > 1 and wire in wire_batteries:
            print('Cut the wire!\n')
        else:
            print('Do NOT cut the wire!')