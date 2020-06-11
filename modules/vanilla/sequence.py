def sequence():
    wire_sequence = [
        {'list': ['c', 'b', 'a', 'ac', 'b', 'ac', 'abc', 'ab', 'b'], 'colour': 'red', 'count': 0},
        {'list': ['b', 'ac', 'b', 'a', 'b', 'bc', 'c', 'ac', 'a'], 'colour': 'blue', 'count': 0},
        {'list': ['abc', 'ac', 'b', 'ac', 'b', 'bc', 'ab', 'c', 'c'], 'colour': 'black', 'count': 0}
    ]
    while True:
        input_raw = input('(Use "x" to quit or "r" to reset)\nUsage <Colour>,<Letter> ').lower().replace(', ', ',').split(',')
        if input_raw[0] == 'x':
            break
        elif input_raw[0] == 'r':
            print('---Reset---\n')
            sequence()
        elif len(input_raw) != 2:
            print('\n--ERROR--\nExpected 2 items!')
            return
        for item in wire_sequence:
            if input_raw[0] == item['colour']:
                if str(input_raw[1]) in item['list'][item['count']]:
                    print('\nCut the wire!\n')
                else:
                    print('\nDo NOT cut the wire!\n')
                item['count']+=1