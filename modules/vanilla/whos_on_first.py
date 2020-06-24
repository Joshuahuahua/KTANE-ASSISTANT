def whos_on_first(input_big, input_small):

    wof_big = [
    {'word': '', 'position': 4},
    {'word': 'BLANK', 'position': 3},
    {'word': 'C', 'position': 1},
    {'word': 'CEE', 'position': 5},
    {'word': 'DISPLAY', 'position': 5},
    {'word': 'FIRST', 'position': 1},
    {'word': 'HOLD_ON', 'position': 5},
    {'word': 'LEAD', 'position': 5},
    {'word': 'LEED', 'position': 4},
    {'word': 'LED', 'position': 2},
    {'word': 'NO', 'position': 5},
    {'word': 'NOTHING', 'position': 2},
    {'word': 'OKAY', 'position': 1},
    {'word': 'READ', 'position': 3},
    {'word': 'REED', 'position': 4},
    {'word': 'RED', 'position': 3},
    {'word': 'SAYS', 'position': 5},
    {'word': 'SEE', 'position': 5},
    {'word': 'THEIR', 'position': 3},
    {'word': 'THERE', 'position': 5},
    {'word': 'THEY_ARE', 'position': 2},
    {'word': 'THEY_RE', 'position': 4},
    {'word': 'UR', 'position': 0},
    {'word': 'YES', 'position': 2},
    {'word': 'YOU', 'position': 3},
    {'word': 'YOU_ARE', 'position': 5},
    {'word': 'YOUR', 'position': 3},
    {'word': 'YOU_RE', 'position':3}]

    wof_small = [
    {'word': 'BLANK', 'list': ['WAIT','RIGHT','OKAY','MIDDLE','BLANK']},
    {'word': 'DONE', 'list': ['SURE','UH_HUH','NEXT','WHAT?','YOUR','UR','YOU_RE','HOLD','LIKE','YOU','U','YOU_ARE','UH_UH','DONE']},
    {'word': 'FIRST', 'list': ['LEFT','OKAY','YES','MIDDLE','NO','RIGHT','NOTHING','UHHH','WAIT','READY','BLANK','WHAT','PRESS','FIRST']},
    {'word': 'HOLD', 'list': ['YOU_ARE','U','DONE','UH_UH','YOU','UR','SURE','WHAT?','YOU_RE','NEXT','HOLD']},
    {'word': 'LEFT', 'list': ['RIGHT','LEFT']},
    {'word': 'LIKE', 'list': ['YOU_RE','NEXT','U','UR','HOLD','DONE','UH_UH','WHAT?','UH_HUH','YOU','LIKE']},
    {'word': 'MIDDLE', 'list': ['BLANK','READY','OKAY','WHAT','NOTHING','PRESS','NO','WAIT','LEFT','MIDDLE']},
    {'word': 'NEXT', 'list': ['WHAT?','UH_HUH','UH_UH','YOUR','HOLD','SURE','NEXT']},
    {'word': 'NO', 'list': ['BLANK','UHHH','WAIT','FIRST','WHAT','READY','RIGHT','YES','NOTHING','LEFT','PRESS','OKAY','NO']},
    {'word': 'NOTHING', 'list': ['UHHH','RIGHT','OKAY','MIDDLE','YES','BLANK','NO','PRESS','LEFT','WHAT','WAIT','FIRST','NOTHING']},
    {'word': 'OKAY', 'list': ['MIDDLE','NO','FIRST','YES','UHHH','NOTHING','WAIT','OKAY']},
    {'word': 'PRESS', 'list': ['RIGHT','MIDDLE','YES','READY','PRESS']},
    {'word': 'READY', 'list': ['YES','OKAY','WHAT','MIDDLE','LEFT','PRESS','RIGHT','BLANK','READY']},
    {'word': 'RIGHT', 'list': ['YES','NOTHING','READY','PRESS','NO','WAIT','WHAT','RIGHT']},
    {'word': 'SURE', 'list': ['YOU_ARE','DONE','LIKE','YOU_RE','YOU','HOLD','UH_HUH','UR','SURE']},
    {'word': 'U', 'list': ['UH_HUH','SURE','NEXT','WHAT?','YOU_RE','UR','UH_UH','DONE','U']},
    {'word': 'UH_HUH', 'list': ['UH_HUH']},
    {'word': 'UH_UH', 'list': ['UR','U','YOU_ARE','YOU_RE','NEXT','UH_UH']},
    {'word': 'UHHH', 'list': ['READY','NOTHING','LEFT','WHAT','OKAY','YES','RIGHT','NO','PRESS','BLANK','UHHH']},
    {'word': 'UR', 'list': ['DONE','U','UR']},
    {'word': 'WAIT', 'list': ['UHHH','NO','BLANK','OKAY','YES','LEFT','FIRST','PRESS','WHAT','WAIT']},
    {'word': 'WHAT', 'list': ['UHHH','WHAT']},
    {'word': 'WHAT', 'list':  ['YOU','HOLD','YOU_RE','YOUR','U','DONE','UH_UH','LIKE','YOU_ARE','UH_HUH','UR','NEXT','WHAT?']},
    {'word': 'YES', 'list': ['OKAY','RIGHT','UHHH','MIDDLE','FIRST','WHAT','PRESS','READY','NOTHING','YES']},
    {'word': 'YOU_ARE', 'list': ['YOUR','NEXT','LIKE','UH_HUH','WHAT?','DONE','UH_UH','HOLD','YOU','U','YOU_RE','SURE','UR','YOU_ARE']},
    {'word': 'YOU', 'list': ['SURE','YOU_ARE','YOUR','YOU_RE','NEXT','UH_HUH','UR','HOLD','WHAT?','YOU,']},
    {'word': 'YOUR', 'list': ['UH_UH','YOU_ARE','UH_HUH','YOUR']},
    {'word': 'YOU_RE', 'list': ['YOU','YOU_RE']}]

    while True:
        #input_big = input('Type "x" to quite.\nPlease input big word (If "", leave blank): ').upper().replace(' ', '_').replace('\'', '_')
        input_big = input_big.upper().replace(' ', '_').replace('\'', '_')
        if input_big[0] == 'x':
            return
        #input_small = input('Please input small words.\nUsage <0 word>, <1 word>...<5 word>: ').upper().replace(', ', ',').replace(' ', '_').split(',')
        input_small = input_small.upper().replace(', ', ',').replace(' ', '_').split(',')
        if len(input_small) != 6:
            print('\n--ERROR--\nExpected 6 items!')
            return

        for wof_big_current in wof_big:
            if input_big == wof_big_current['word']:
                for wof_small_current in wof_small:
                    if wof_small_current['word'] == input_small[wof_big_current['position']]:
                        for i, word in enumerate(wof_small_current['list']):
                            if word in input_small:
                                print('Press: ' + str(word))
                                return
            

        print('---ERROR---\n That word can not be found!')
    return