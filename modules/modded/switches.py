#Coded by Joshuahuahua
def switches():
    avoid_switches = [
    [False,False,True,False,False],
    [False,True,False,True,True],
    [False,True,True,True,True],
    [True,False,False,True,False],
    [True,False,False,True,True],
    [True,False,True,True,True],
    [True,True,False,False,False],
    [True,True,False,True,False],
    [True,True,True,False,False],
    [True,True,True,True,False]]

    switches_input = input('Usage <switch1pos, switch2pos, etc> (U/D): ').lower().replace(', ', ',').split(',')
    light_input = input('Usage <light1pos, light2pos, etc> (U/D): ').lower().replace(', ', ',').split(',')
    if len(switches_input) != 5 or len(switches_input) != 5:
        print('\n--ERROR--\nExpected 5 items!')
        return  

    for i in range(0,5):
        if switches_input[i] == 'u': switches_input[i] = True
        elif switches_input[i] == 'd': switches_input[i] = False
        if light_input[i] == 'u': light_input[i] = True
        elif light_input[i] == 'd': light_input[i] = False
        else:
            print('---ERROR---\nInvalid input. Expected u/d')
            return

    while switches_input != light_input:
        change_made = False
        for i, item in enumerate(switches_input):
            if switches_input[i] != light_input[i]:
                switches_input[i] = not switches_input[i]
                if switches_input not in avoid_switches:
                    print('Click Switch', i+1)
                    change_made = True
                else:
                    switches_input[i] = not switches_input[i]
        
        if change_made == False:
            for i, item in enumerate(switches_input):
                if switches_input[i] == light_input[i]:
                    switches_input[i] = not switches_input[i]
                    if switches_input not in avoid_switches:
                        print('Click Switch', i+1)
                        break
                    else:
                        switches_input[i] = not switches_input[i]