#Coded by Joshuahuahua
def switches():
    
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

    switches_input = input('Usage <switch1pos, switch2pos, etc> (U/D): ').lower().replace(', ', ',').split(',')
    if len(switches_input) != 6:
        print('\n--ERROR--\nExpected 6 items!')
        return  
    light_input = input('Usage <light1pos, light2pos, etc> (U/D): ').lower().replace(', ', ',').split(',')
    if len(switches_input) != 6:
        print('\n--ERROR--\nExpected 6 items!')
        return

    for i, item in enumerate(switches_input):
        if item == 'u': switches_input[i] = True
        elif item == 'd': switches_input[i] = False
    for i, item in enumerate(light_input):
        if item == 'u': light_input[i] = True
        elif item == 'd': light_input[i] = False
    
    
    print(switches_input)
    print(light_input)

switches()

'''

    while True:
        for x in switch:
            if light[0] != switch[0]:
                if switch[0] == 'D':
                    switch[0] = 'U'
                    if switch in avoid_switches:
                        switch[0] = 'D' 
                    else:
                        print('move 1st switch')
                elif switch[0] == 'U':
                    switch[0] = 'D' 
                    if switch in avoid_switches:
                        switch[0] = 'U'
                    else:
                        print('move 1st switch')
                      

            if light[1] != switch[1]:
                if switch[1] == 'D':
                    switch[1] = 'U'
                    if switch in avoid_switches:
                        switch[1] = 'D'    
                    else:
                        print('move 2nd switch')
                elif switch[1] == 'U':
                    switch[1] = 'D' 
                    if switch in avoid_switches:
                        switch[1] = 'U'
                    else:
                        print('move 2nd switch')
            
            if light[2] != switch[2]:
                if switch[2] == 'D':
                    switch[2] = 'U'
                    if switch in avoid_switches:
                        switch[2] = 'D' 
                    else:
                        print('move 3rd switch')
                elif switch[2] == 'U':
                    switch[2] = 'D' 
                    if switch in avoid_switches:
                        switch[2] = 'U'
                    else:
                        print('move 3rd switch')
                     
            
            
            if light[3] != switch[3]:
                if switch[3] == 'D':
                    switch[3] = 'U'
                    if switch in avoid_switches:
                        switch[3] = 'D' 
                    else:
                        print('move 4th switch')
                elif switch[3] == 'U':
                    switch[3] = 'D' 
                    if switch in avoid_switches:
                        switch[3] = 'U'
                    else:
                        print('move 4th switch')
                       
            
            if light[4] != switch[4]:
                if switch[4] == 'D':
                    switch[4] = 'U'
                    if switch in avoid_switches:
                        switch[4] = 'D' 
                    else:
                        print('move 5th switch')
                       
                elif switch[4] == 'U':
                    switch[4] = 'D' 
                    if switch in avoid_switches:
                        switch[4] = 'U'
                    else:
                        print('move 5th switch')   
        break

'''