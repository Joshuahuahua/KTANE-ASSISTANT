def knob():
    dic = [
    {'count': '0', 'dir_word': 'left', 'dir_num': 4},
    {'count': '1', 'dir_word': 'left', 'dir_num': 4},
    {'count': '3', 'dir_word': 'down', 'dir_num': 3},
    {'count': '4', 'dir_word': 'up', 'dir_num': 1},
    {'count': '5', 'dir_word': 'down', 'dir_num': 3},
    {'count': '5U', 'dir_word': 'right', 'dir_num': 2}
    ]

    try:
        knob = input('Number of lit LED\'s on left\nUsage <"UP" direction><1-5/5U>: ').upper().replace(', ', ',').split(',')
        if len(knob) != 2:
            print('\n--ERROR--\nExpected 2 items!')
            return
        # Convert word to num
        for i, dic_item in enumerate(dic):
            if knob[0] == dic[i]['dir_word']:
                knob[0] = dic[i]['dir_num']
        # Add diffuse direction and wrap.
        for i, dic_item in enumerate(dic):
            if knob[1] == dic[i]['count']:
                knob[0]+=dic[i]['dir_num']-1
                if knob[0]>4:
                    knob[0]-=4
        # Return direction answer
        for i, dic_item in enumerate(dic):
            if knob[0] == dic[i]['dir_num']:
                print('Face the knob: ' + str(dic[i]['dir_word']))
                return
        raise
    except:
        print('---ERROR---\nCould not calculate answer!')