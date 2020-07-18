###################################### VANILLA ######################################
from modules.vanilla.simple_wires import simple_wires
from modules.vanilla.button import button
from modules.vanilla.symbols import symbols
from modules.vanilla.simon_says import simon_says
from modules.vanilla.memory import memory
from modules.vanilla.password import password
from modules.vanilla.sequence import sequence
from modules.vanilla.complex_wires import complex_wires
from modules.vanilla.knob import knob
from modules.vanilla.whos_on_first import whos_on_first
from modules.vanilla.morse import morse
from modules.vanilla.maze import maze
###################################### MODDED ######################################
from modules.modded.colour_flash import colour_flash
from modules.modded.combination_locks import combination_locks
from modules.modded.festive_piano_keys import festive_piano_keys
from modules.modded.emoji_math import emoji_math
#from modules.modded.BLANK import BLANK
from modules.modded.piano_keys import piano_keys
#from modules.modded.BLANK import BLANK
from modules.modded.switches import switches
from modules.modded.two_bits import two_bits
from modules.modded.word_scramble_anagram import word_scramble_anagram
'''
from modules.modded.BLANK import BLANK
from modules.modded.BLANK import BLANK
from modules.modded.BLANK import BLANK
'''

def assign_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print('Please enter a whole number')



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

    bat_b = assign_int('Number of big batteries: ')
    
    print('Enter the labels of the LIT indicators (Enter nothing to continue/skip)')
    while True:
        user_input = input('> ')
        if user_input == '':
            break
        else:
            ind_lit.append(user_input)

    print('Enter the labels of the UNLIT indicators (Enter nothing to continue/skip)')
    while True:
        user_input = input('> ')
        if user_input == '':
            break
        else:
            ind_unlit.append(user_input)

    while True:
        try:
            serial_odd = False if int(serial[-1]) %2 == 0 else True
            serial_vowel = True if any(x in serial for x in ['A', 'E', 'I', 'O', 'U']) else False
            break
        except:
            print('---ERROR---\nPlease input a valid serial number!')

    port_parallel = assign_int('How many parallel ports are there?: ')
       
    port_dvi = assign_int('How many DVI ports are there?: ')
       
    port_ps2 = assign_int('How many PS2 ports are there?: ')
       
    port_rj45 = assign_int('How many RJ45 ports are there?: ')
       
    port_serial = assign_int('How many Serial ports are there?: ')
       
    port_rca = assign_int('How many RCA ports are there?: ')
        
    port_plate = assign_int('How many port plates are there?: ')
    
    bomb_data = {
        'bat_AA': bat_aa,
        'bat_B': bat_b,
        'bat_total': bat_aa+bat_b,
        'ind_LIT': ind_lit,
        'ind_UNLIT': ind_unlit,
        'serial': serial,
        'serial_odd': serial_odd,
        'serial_vowel': serial_vowel,
        'port_parallel': port_parallel,
        'port_dvi': port_dvi,
        'port_ps2': port_ps2,
        'port_rj45': port_rj45,
        'port_serial': port_serial,
        'port_rca': port_rca,
        'port_total': port_parallel+port_dvi+port_ps2+port_rj45+port_serial+port_rca
        'port_plate': port_plate,
        'strikes': 0
        'modules_total': 101,
        'modules_solved': 0,
    }

    print('\n-----Setup Complete-----')
    return bomb_data

bomb_data = init()

while True:
    print('\n------------------------------------------')
    print('Keep Talking and Nobody Explodes Assistant')
    print('            Modules Solved: ' + str(bomb_data['modules_solved']))
    print('               Strikes: ' + str(bomb_data['strikes']))
    print('------------------------------------------\n')

    user_input = input('Enter a module (type "help" for options) > ').lower()
    
###################################### VANILLA ######################################

    if user_input == 'solved':
        bomb_data['modules_solved']+=1
    if user_input[:8] == 'strikes ':
        bomb_data['strikes'] = user_input[-1]
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
        
###################################### MODDED ######################################

    elif user_input == 'two bits':
        two_bits(bomb_data)
    elif user_input == 'combination lock' or user_input == 'combination locks':
        combination_locks(bomb_data)
    elif user_input == 'word scramble' or user_input == 'anagram':
        word_scramble_anagram()
    elif user_input == 'emoji math':
        emoji_math()
    elif user_input == 'festive piano keys':
        festive_piano_keys(bomb_data)
    elif user_input == 'piano keys':
        piano_keys(bomb_data)
    elif user_input == 'colour flash':
        colour_flash()
    elif user_input == 'switches':
        switches()


    elif user_input == 'help':
        print('\n------OPTIONS------')
        print('Simple Wires, Button, Symbols, Memory')
        print('Password, Sequence, Complex Wires, Knob')
        print('Who\'s on first, Morse code')
        print('-------------------')
    elif user_input == 'quit':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice!')