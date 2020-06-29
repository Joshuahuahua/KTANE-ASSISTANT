#designed by Matthew Alphonso
def simon_states():
    colours = ['red', 'blue', 'green', 'yellow']
    priority = [{'top_left': 'red','highest': 'red', 'high': 'blue' ,'low': 'green','lowest': 'yellow'},
    {'top_left': 'yellow','highest': 'blue','high': 'yellow','low': 'red','lowest': 'green'},
    {'top_left': 'green','highest': 'green','high': 'red','low': 'yellow','lowest': 'blue'},
    {'top_left': 'blue','highest': 'yellow','high': 'green','low': 'blue','lowest': 'red'}]
    while True:
        user_input = input('what is the top left colour?')
        if user_input not in colours:
            print('\nInvalid colour')
            break
        for i, x in enumerate(priority):
                if user_input in priority[i]['top_left']:
                    current_priority = priority[i]



        #stage 1 
        stage1_flash = input('what colour/colours are flashing?').lower().replace(', ', ',').split(',')
        #add error
        if len(stage1_flash) == 1:
                print('press', stage1_flash[0])
                stage1_flash = 'press', stage1_flash[0]
        elif len(stage1_flash) == 2 and 'blue' in stage1_flash:
            print('press', current_priority['highest'])
            stage1_flash = 'press', current_priority['highest']
        elif len(stage1_flash) == 2 and 'blue' not in stage1_flash:
            print('press blue')
            stage1_flash = 'press blue'
        elif len(stage1_flash) == 3 and 'red' in stage1_flash:
            print('press', current_priority['lowest'])
            stage1_flash = 'press', current_priority['lowest']
        elif len(stage1_flash) == 3 and 'red' not in stage1_flash:
            print('press red')
            stage1_flash =
        else:
            print('press', current_priority['high'])

        #stage 2 
        stage2_flash = input('what colour/colours are flashing?').lower().replace(', ', ',').split(',')
        #add error 
        if len(stage2_flash) == 2 and 'red' in stage2_flash and 'blue' in stage2_flash:
            if 'red' not in current_priority['highest'] and 'blue' not in current_priority['highest']:
                print('press',current_priority['highest'])
            elif 'red' not in current_priority['high'] and 'blue' not in current_priority['high']:
                print('press',current_priority['high'])
            else:
                print('press',current_priority['low'])

        elif len(stage2_flash) == 2:
            if current_priority['lowest'] not in stage2_flash:
                print('press',current_priority['lowest'] )
            elif current_priority['low'] not in stage2_flash:
                print('press',current_priority['low'] )            
            else:
                print('press',current_priority['high'])
        elif len(stage2_flash) == 2 and 'blue' not in stage2_flash:
            print('press blue')
        elif len(stage2_flash) == 1:
            print('press yellow')
        elif 'red' in stage2_flash and 'blue' in stage2_flash and 'green' in stage2_flash and 'yellow' in stage2_flash:
            #mistake print('press', stage1_flash)




simon_states()