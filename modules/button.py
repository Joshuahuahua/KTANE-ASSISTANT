def button(bomb_data):
    button_raw = input('Usage <colour, word>: ').lower().split(", ")
    if len(button_raw) != 2:
        print('\n--ERROR--\nExpected 2 items!')
        return
    
    colour = button_raw[0]
    word = button_raw[1]

    if button_raw == ['red', 'hold'] or word == 'detonate' and bomb_data['bat_total'] > 1 or 'FRK' in bomb_data['ind_LIT'] and bomb_data['bat_total'] > 2:
        print('\nPRESS and then immediately release the button!')
    else:
        print('\nHOLD the button!\n')
        stripe = input('What colour is the stripe: ').lower()
        if stripe == 'blue':
            print('\nRelease button when countdown contains a 4')
        elif stripe == 'yellow': 
            print('\nRelease button when countdown contains a 5')
        else:
            print('\nRelease button when countdown contains a 1')