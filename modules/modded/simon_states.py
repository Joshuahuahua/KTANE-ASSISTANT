#designed by Matthew Alphonso
#NEEDS REFINING
def simon_states():
    colours = ['red', 'blue', 'green', 'yellow']
    not_pressed['red','blue','green','yellow']
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
            stage1_flash = stage1_flash[0]
            not_pressed.remove(stage1_flash[0])
        elif len(stage1_flash) == 2 and 'blue' in stage1_flash:
            print('press', current_priority['highest'])
            stage1_flash = current_priority['highest']
            not_pressed.remove(current_priority['highest'])
        elif len(stage1_flash) == 2 and 'blue' not in stage1_flash:
            print('press blue')
            stage1_flash = 'blue'
            not_pressed.remove('blue')
        elif len(stage1_flash) == 3 and 'red' in stage1_flash:
            print('press', current_priority['lowest'])
            stage1_flash = current_priority['lowest']
            not_pressed.remove(current_priority['lowest'])
        elif len(stage1_flash) == 3 and 'red' not in stage1_flash:
            print('press red')
            stage1_flash = 'red'
            not_pressed.remove('red')
        else:
            print('press', current_priority['high'])
            stage1_flash = current_priority['high']
            not_pressed.remove(current_priority['high'])
        
        #stage 2 
        stage2_flash = input('what colour/colours are flashing?').lower().replace(', ', ',').split(',')
        #add error 
        if len(stage2_flash) == 2 and 'red' in stage2_flash and 'blue' in stage2_flash:
            if 'red' not in current_priority['highest'] and 'blue' not in current_priority['highest']:
                print('press',current_priority['highest'])
                stage2_flash = current_priority['highest']
                not_pressed.remove(current_priority['highest'])
            elif 'red' not in current_priority['high'] and 'blue' not in current_priority['high']:
                print('press',current_priority['high'])
                stage2_flash = current_priority['high']
                not_pressed.remove(current_priority['high'])
            else:
                print('press',current_priority['low'])
                stage2_flash = current_priority['low']
                not_pressed.remove(current_priority['low'])

        elif len(stage2_flash) == 2:
            if current_priority['lowest'] not in stage2_flash:
                print('press',current_priority['lowest'])
                stage2_flash = current_priority['lowest']
                not_pressed.remove(current_priority['lowest'])
            elif current_priority['low'] not in stage2_flash:
                print('press',current_priority['low'])  
                stage2_flash = current_priority['low'] 
                not_pressed.remove(current_priority['low'] )        
            else:
                print('press',current_priority['high'])
                stage2_flash = current_priority['high']
                not_pressed.remove(current_priority['high'])
        elif len(stage2_flash) == 2 and 'blue' not in stage2_flash:
            print('press blue')
            stage2_flash = 'blue'
            not_pressed.remove('blue')
        elif len(stage2_flash) == 1:
            print('press yellow')
            stage2_flash = 'yellow'
            not_pressed.remove('yellow')
        elif 'red' in stage2_flash and 'blue' in stage2_flash and 'green' in stage2_flash and 'yellow' in stage2_flash:
            print('press', stage1_flash)
            stage2_flash = stage1_flash
            not_pressed.remove(stage1_flash)
        else:
            for i, item in enumerate(colours):
                if colours[i] not in stage2_flash:
                    print('press', colours[i])
                    stage2_flash = colours[i]
                    not_pressed.remove(colours[i])
        
        #stage 3       
        stage3_flash = input('what colour/colours are flashing?').lower().replace(', ', ',').split(',')
        #import error 
        if len(stage3_flash) == 3 and (stage1_flash in stage3_flash or stage2_flash in stage3_flash):
            if current_priority['highest'] in stage3_flash and (current_priority['highest'] in stage1_flash or current_priority['highest'] in stage2):
                print('press', current_priority['highest'])
                stage3_flash = current_priority['highest']
                not_pressed.remove(current_priority['highest'])
            elif current_priority['high'] in stage3_flash and (current_priority['high'] in stage1_flash or current_priority['high'] in stage2):  
                print('press', current_priority['high'])
                stage3_flash = current_priority['high']
                not_pressed.remove(current_priority['high'])
            elif current_priority['low'] in stage3_flash and (current_priority['low'] in stage1_flash or current_priority['low'] in stage2):  
                print('press', current_priority['low'])
                stage3_flash = current_priority['low']
                not_pressed.remove(current_priority['low'])
            elif current_priority['lowest'] in stage3_flash and (current_priority['lowest'] in stage1_flash or current_priority['lowest'] in stage2):  
                print('press', current_priority['lowest'])
                stage3_flash = current_priority['lowest']
                not_pressed.remove(current_priority['lowest'])
        elif len(stage3_flash) == 3:
            if current_priority['highest'] in stage3_flash:
                print('press', current_priority['highest'])
                stage3_flash = current_priority['highest']
                not_pressed.remove(current_priority['highest'])
            elif current_priority['high'] in stage3_flash:
                print('press', current_priority['high'])
                stage3_flash = current_priority['high']
                not_pressed.remove(current_priority['high'])
            elif current_priority['low'] in stage3_flash:
                print('press', current_priority['low'])
                stage3_flash = current_priority['low']
                not_pressed.remove(current_priority['low'])
            elif current_priority['lowest'] in stage3_flash:
                print('press', current_priority['lowest'])
                stage3_flash = current_priority['lowest']
                not_pressed.remove(current_priority['lowest'])
        elif len(stage3_flash) == 2 and stage1_flash in stage3_flash and stage2_flash in stage3_flash:
            if current_priority['lowest'] not in stage3_flash:
                print('press',current_priority['lowest'])
                stage3_flash = current_priority['lowest']
                not_pressed.remove(current_priority['lowest'])
            elif current_priority['low'] not in stage3_flash:
                print('press', current_priority['low'])
                stage3_flash = current_priority['low']
                not_pressed.remove(current_priority['low'])
            elif current_priority['high'] not in stage3_flash:
                print('press', current_priority['high'])
                stage3_flash = current_priority['high']
                not_pressed.remove(current_priority['high'])
        elif len(stage3_flash) == 2:
            print('press', stage1_flash)
            stage3_flash = stage1_flash
            not_pressed.remove(stage1_flash)
        elif len(stage3_flash) == 1:
            print('press', stage3_flash[0])
            stage3_flash = stage3_flash[0]
            not_pressed.remove(stage3_flash[0])
        else:
            print('press',current_priority['low'])
            stage3_flash = current_priority['low']
            not_pressed.remove(current_priority['low'])
 
        #stage 4       
        stage4_flash = input('what colour/colours are flashing?').lower().replace(', ', ',').split(',')
        #import error
        if stage1_flash not in stage2_flash and stage1_flash not in stage3_flash and stage2_flash not in stage3_flash:
            for i, item in enumerate(colours):
                if stage1_flash not in colours[i] and stage2_flash not in colours[i] and stage3_flash not in colours[i]:
                    print('press',colours[i]) 
        
        #elif if three colours flashed and exactly one hasn't been pressed, press that colour.

        
        elif len(stage4_flash) >= 3:
            print('press',current_priority['lowest'])
        elif len(stage4_flash) == 1:  
            print('press',stage4_flash[0]) 
        else:
            print('press green')

simon_states()