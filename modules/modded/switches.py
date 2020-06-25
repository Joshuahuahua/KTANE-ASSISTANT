#made by Matthew Alphonso
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
    light = []
    #position of switches 
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
    
    #position of lights 
    while True:   
        light1 = input('\nposition of 1st light: ').upper()
        if light1 == 'D' or light1 == 'U':
            light.append(light1)
            break
        else:
            print('Type D or U')
    while True:   
        light2 = input('\nposition of 2nd light: ').upper()
        if light2 == 'D' or light2 == 'U':
            light.append(light2)
            break
        else:
            print('Type D or U')
    
    while True:   
        light3 = input('\nposition of 3rd light: ').upper()
        if light3 == 'D' or light3 == 'U':
            light.append(light3)
            break
        else:
            print('Type D or U')
    
    while True:   
        light4 = input('\nposition of 4th light: ').upper()
        if light4 == 'D' or light4 == 'U':
            light.append(light4)
            break
        else:
            print('Type D or U')
    
    while True:   
        light5 = input('\nposition of 5th light: ').upper()
        if light5 == 'D' or light5 == 'U':
            light.append(light5)
            break
        else:
            print('Type D or U')

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

