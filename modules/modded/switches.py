def switch_mod():
    
    avoid_switches = [
    ['D','D','U','D','D'],
    ['D','U','D','U','U'],
    ['D','U','U','U','U'],
    ['U','D','D','U','D'],
    ['U','D','D','U','U'],
    ['U','U','D','D','D'],
    ['U','U','D','U','D'],
    ['U','U','U','D','D'],
    ['U','U','U','U','D']]

    switch= []
    while True:
        user1 = input('\nposition of 1st switch: ').upper()
        if user1 == 'D' or user1 == 'U':
            switch.append(user1)
            break
        else:
            print('Type D or U')

    while True:
        user2 = input('\nposition of 2nd switch: ').upper()
        if user2 == 'D' or user2 == 'U':
            switch.append(user2)
            break
        else:
            print('Type D or U')

    while True:
        user3 = input('\nposition of 3rd switch: ').upper()
        if user3 == 'D' or user3 == 'U':
            switch.append(user3)
            break
        else:
            print('Type D or U')

    while True:
        user4 = input('\nposition of 4th switch: ').upper()
        if user4 == 'D' or user4 == 'U':
            switch.append(user4)
            break
        else:
            print('Type D or U')

    while True:   
        user5 = input('\nposition of 5th switch: ').upper()
        if user5 == 'D' or user5 == 'U':
            switch.append(user5)
            break
        else:
            print('Type D or U')
    
    
    while True:
        print('\n',switch)
        move = input('Which switch to move: 1, 2, 3, 4, 5, or finish:')
        if move == '1':
            if switch[0] == 'D':
                switch[0] = 'U'
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[0] = 'D' 
            elif switch[0] == 'U':
                switch[0] = 'D' 
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[0] = 'U'

        elif move =='2':
            if switch[1] == 'D':
                switch[1] = 'U'
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[1] = 'D' 
            elif switch[1] == 'U':
                switch[1] = 'D' 
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[1] = 'U' 

        elif move =='3':
            if switch[2] == 'D':
                switch[2] = 'U'
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[2] = 'D' 
            elif switch[2] == 'U':
                switch[2] = 'D' 
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[2] = 'U' 

        elif move =='4':
            if switch[3] == 'D':
                switch[3] = 'U'
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[3] = 'D' 
            elif switch[3] == 'U':
                switch[3] = 'D'  
                if switch in avoid_switches:
                    print('\nAVOID SWITCH') 
                    switch[3] = 'U'
        
        elif move =='5':
            if switch[4] == 'D':
                switch[4] = 'U'
                if switch in avoid_switches:
                    print('\nAVOID SWITCH')
                    switch[4] = 'D' 
            elif switch[4] == 'U':
                switch[4] = 'D'  
                if switch in avoid_switches:
                    print('\nAVOID SWITCH') 
                    switch[4] = 'U'
        
        elif move == 'finish':
            print('\nFinished')
            break
        else:
            print('\nInvalid input')
            

switch_mod()
