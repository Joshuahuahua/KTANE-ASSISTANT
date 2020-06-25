#Coded by Joshuahuahua
def memory():
    stored_memory = []
    #1 1234
    data = [
        [
            {'method': 'position', 'value': 2},
            {'method': 'position', 'value': 2},
            {'method': 'position', 'value': 3},
            {'method': 'position', 'value': 4}
        ],
        [
            {'method': 'literal', 'value': 4},
            {'method': 'stage', 'stage': 1, 'value': 'position'},
            {'method': 'position', 'value': 1},
            {'method': 'stage', 'stage': 1, 'value': 'position'}
        ],
        [
            {'method': 'stage', 'stage': 2, 'value': 'label'},
            {'method': 'stage', 'stage': 1, 'value': 'label'},
            {'method': 'position', 'value': 3},
            {'method': 'literal', 'value': 4}
        ],
        [
            {'method': 'stage', 'stage': 1, 'value': 'position'},
            {'method': 'position', 'value': 1},
            {'method': 'stage', 'stage': 2, 'value': 'position'},
            {'method': 'stage', 'stage': 2, 'value': 'position'}
        ],
        [
            {'method': 'stage', 'stage': 1, 'value': 'label'},
            {'method': 'stage', 'stage': 2, 'value': 'label'},
            {'method': 'stage', 'stage': 4, 'value': 'label'},
            {'method': 'stage', 'stage': 3, 'value': 'label'}
        ]
    ]

    for i in range(0, 5):
        while True:
            try:
                memory_raw = int(input('Input main number followed by 4 smaller numbers: '))
                if len(memory_raw) != 5:
                    raise
                break
            except:
                print('--ERROR--\nExpected a 5-digit number!')

        if data[i][int(memory_raw[0])-1]['method'] == 'position':
            label = memory_raw[data[i][int(memory_raw[0])-1]['value']]
            position = data[i][int(memory_raw[0])-1]['value']
        
        elif data[i][int(memory_raw[0])-1]['method'] == 'literal':
            label = data[i][int(memory_raw[0])-1]['value']
            position = memory_raw.index(str(data[i][int(memory_raw[0])-1]['value']))
        
        elif data[i][int(memory_raw[0])-1]['method'] == 'stage':
            
            if data[i][int(memory_raw[0])-1]['value'] == 'label':
                label = stored_memory[data[i][int(memory_raw[0])-1]['stage']-1]['label']
                position = memory_raw.index(str(stored_memory[data[i][int(memory_raw[0])-1]['stage']-1]['label']))
            
            elif data[i][int(memory_raw[0])-1]['value'] == 'position':
                label = memory_raw[stored_memory[data[i][int(memory_raw[0])-1]['stage']-1]['position']]
                position = stored_memory[data[i][int(memory_raw[0])-1]['stage']-1]['position']


        stored_memory.append({'label': label, 'position': position})
        print('Press:', label)
        #print(stored_memory)
