from modules.wires import wires
from modules.button import button
from modules.symbols import symbols

while True:
    print('------------------------------------------')
    print('Keep Talking and Nobody Explodes Assistant')
    print('------------------------------------------\n')

    bomb_data = {
        'bat_AA': 0,
        'bat_B': 0,
        'bat_total': 0,
        'ind_LIT': [],
        'ind_UNLIT': [],
        'serial': '',
        'serial_odd': False,
        'serial_vowel': False,
        'port_DVI': False,
        'port_parallel': False,
        'port_ps2': False,
        'port_rj45': False,
        'port_rca': False,
    } 

    user_input = input('Enter a module (type "help" for options) > ').lower()
    if user_input == 'wires':
        wires(bomb_data)
    elif user_input == 'button':
        button(bomb_data)
    elif user_input == 'symbols':
        symbols(bomb_data)
    elif user_input == 'help':
        print('\n------OPTIONS------')
        print('Wires, Button, Symbols')
        print('-------------------\n')
    elif user_input == 'quit':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice!\n')

