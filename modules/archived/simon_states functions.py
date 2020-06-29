#stage 1 
        stage1_answer = stage1(input('what colour/colours are flashing?').lower().replace(', ', ',').split(','))
        print('press', stage1_answer)
        not_pressed.remove(stage1_answer)
        #add error

        #stage 2
        stage2_answer = stage2(input('what colour/colours are flashing?').lower().replace(', ', ',').split(','))
        print('press', stage2_answer)
        not_pressed.remove(stage2_answer)
        #add error






def stage1(stage1_flash):
    if len(stage1_flash) == 1:
        return stage1_flash[0]
    elif len(stage1_flash) == 2 and 'blue' in stage1_flash:
        return current_priority['highest']
    elif len(stage1_flash) == 2 and 'blue' not in stage1_flash:
        return 'blue'
    elif len(stage1_flash) == 3 and 'red' in stage1_flash:
        return current_priority['lowest']
    elif len(stage1_flash) == 3 and 'red' not in stage1_flash:
        return 'red'
    else:
        return current_priority['high']

def stage2(stage2_flash)
    if len(stage2_flash) == 2 and 'red' in stage2_flash and 'blue' in stage2_flash:
        if 'red' not in current_priority['highest'] and 'blue' not in current_priority['highest']:
            return current_priority['highest']
        elif 'red' not in current_priority['high'] and 'blue' not in current_priority['high']:
            return current_priority['high']
        else:
            return current_priority['low']
    elif len(stage2_flash) == 2:
        if current_priority['lowest'] not in stage2_flash:
            return current_priority['lowest']
        elif current_priority['low'] not in stage2_flash:
            return current_priority['low'] 
        else:
            return current_priority['high']
    elif len(stage2_flash) == 2 and 'blue' not in stage2_flash:
        return 'blue'
    elif len(stage2_flash) == 1:
        return 'yellow'
    elif 'red' in stage2_flash and 'blue' in stage2_flash and 'green' in stage2_flash and 'yellow' in stage2_flash:
        return stage1_flash
    else:
        for i, item in enumerate(colours):
            if colours[i] not in stage2_flash:
                return colours[i]