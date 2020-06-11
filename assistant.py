from modules.vanilla.simple_wires import simple_wires
from modules.vanilla.button import button
from modules.vanilla.symbols import symbols
from modules.vanilla.memory import memory
from modules.vanilla.password import password
from modules.vanilla.sequence import sequence
from modules.vanilla.complex_wires import complex_wires
from modules.vanilla.knob import knob


while True:
    print('\n------------------------------------------')
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
    if user_input == 'simple wires' or user_input == 'simple_wires':
        simple_wires(bomb_data)
    elif user_input == 'button':
        button(bomb_data)
    elif user_input == 'symbols':
        symbols()
    elif user_input == 'memory':
        memory()
    elif user_input == 'password':
        password()
    elif user_input == 'sequence':
        sequence()
    elif user_input == 'complex wires' or user_input == 'complex_wires':
        complex_wires(bomb_data)
    elif user_input == 'knob':
        knob()
    
    elif user_input == 'help':
        print('\n------OPTIONS------')
        print('Simple Wires, Button, Symbols, Memory')
        print('Password, Sequence, Complex Wires, Knob')
        print('-------------------')
    elif user_input == 'quit':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice!')