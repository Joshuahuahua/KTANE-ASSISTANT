def button(bomb_data):
    button_raw = input('Usage <colour, word>: ').lower().split(", ")
    colour = button_raw[0]
    word = button_raw[1]

    if button_raw == ['red', 'hold'] or word == 'detonate' and bomb_data['bat_total'] > 1 or 'FRK' in bomb_data['ind_LIT'] and bomb_data['bat_total'] > 2:
        print('PRESS and then immediately release the button!')
    else:
        print('HOLD the button!')
        stripe = input('What is the colour: ').lower()
        if stripe == 'blue':
            print('Release button when countdown contains a 4')
        elif stripe == 'yellow': 
            print('Release button when countdown contains a 5')
        else:
            print('Release button when countdown contains a 1')