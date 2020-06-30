def button(bomb_data, button_word, button_colour):
    #button_raw = input('Usage <colour, word>: ').lower().replace(', ', ',').split(',')
    button_raw = [button_colour, button_word]

    if button_raw == ['red', 'hold'] or button_word == 'detonate' and bomb_data['bat_total'] > 1 or 'FRK' in bomb_data['ind_LIT'] and bomb_data['bat_total'] > 2:
        return 'Press'
    else:
        return 'Hold'

def button2(stripe):
    if stripe == 'blue':
        return 4
    elif stripe == 'yellow': 
        return 5
    else:
        return 1