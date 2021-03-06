###################################### VANILLA ######################################
from modules.simple_wires import simple_wires
from modules.button import button
from modules.symbols import symbols
from modules.simon_says import simon_says
from modules.memory import memory
from modules.password import password
from modules.sequence import sequence
from modules.complex_wires import complex_wires
from modules.knob import knob
from modules.whos_on_first import whos_on_first
from modules.morse import morse
from modules.maze import maze


def init():
    ind_lit = []
    ind_unlit = []
    print('-----Setup Initializing-----')
    while True:
        try:
            bat_aa = int(input('Number of idividual AA batteries: '))
            if (bat_aa % 2) == 0:
                break
            else:
                print('Please enter an even number (AA Batteries always come in pairs)')
                continue
        except ValueError:
            print('Please enter a whole number')
            pass

    while True:
        try:
            bat_b = int(input('Number of big batteries: '))
            break
        except ValueError:
            print('Please enter a whole number')
            pass

    while True:
        user_input = input('Enter the labels of the LIT indicators (Enter nothing to continue/skip): ')
        if user_input == '':
            break
        else:
            ind_lit.append(user_input)

    while True:
        user_input = input('Enter the labels of the UNLIT indicators (Enter nothing to continue/skip): ')
        if user_input == '':
            break
        else:
            ind_unlit.append(user_input)

    while True:
        try:
            serial = input('Serial number: ').upper()
            serial_odd = True
            if (int(serial[-1]) % 2) == 0:
                serial_odd = False
            break
        except:
            print('---ERROR---\nPlease input a valid serial number!')

    vowels = set('AEIOU')
    serial_vowel = False
    for vowel in vowels:
        if vowel in serial:
            serial_vowel = True

    if input('Is there a parallel port? (Y/N): ').lower() == 'y':
        port_parallel = True
    else:
        port_parallel = False  

    bomb_data = {
        'bat_AA': bat_aa,
        'bat_B': bat_b,
        'bat_total': bat_aa+bat_b,
        'ind_LIT': ind_lit,
        'ind_UNLIT': ind_unlit,
        'serial': serial,
        'serial_odd': serial_odd,
        'serial_vowel': serial_vowel,
        'port_parallel': port_parallel
    }

    print('\n-----Setup Complete-----')
    return bomb_data

bomb_data = init()

while True:
    print('\n------------------------------------------')
    print('Keep Talking and Nobody Explodes Assistant')
    print('------------------------------------------')

    user_input = input('Enter a module (type "help" for options) > ').lower()
    
###################################### VANILLA ######################################

    if user_input == 'simple wires' or user_input == 'simple_wires':
        simple_wires(bomb_data)
    elif user_input == 'button':
        button(bomb_data)
    elif user_input == 'symbols':
        symbols()
    elif user_input == 'simon says':
        simon_says(bomb_data)
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
    elif user_input == 'whos on first' or user_input == 'who\'s on first' or user_input == 'wof':
        whos_on_first()
    elif user_input == 'morse' or user_input == 'morse code':
        morse()
    elif user_input == 'maze':
        maze()

    elif user_input == 'help':
        print('\n-----------------OPTIONS-----------------')
        print('Simple Wires, Button, Symbols, Simon Says')
        print('Memory, Password, Sequence, Complex Wires')
        print('Knob, Who\'s on first, Morse code, Maze')
        print('-----------------------------------------')
    elif user_input == 'quit':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice!')