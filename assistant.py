from modules.vanilla.simple_wires import simple_wires
from modules.vanilla.button import button
from modules.vanilla.symbols import symbols
from modules.vanilla.memory import memory
from modules.vanilla.password import password
from modules.vanilla.sequence import sequence
from modules.vanilla.complex_wires import complex_wires
from modules.vanilla.knob import knob
from modules.vanilla.whos_on_first import whos_on_first

ind_lit = []
ind_unlit = []

# List of unlit/lit (2 seperate lists) indicators. all caps
# Serial number
# Number of big batteries
# Number of double A batteries
while True:
    try:
        aabatteries = int(input('Number of idividual AA batteries: '))
        if (aabatteries % 2) == 0:
            break
        else:
            print('Please enter an even number (AA Batteries always come in pairs)')
            continue
    except ValueError:
        print('Please enter a whole number')
        pass

while True:
    try:
        bigbatteries = int(input('Number of big batteries: '))
        break
    except ValueError:
        print('Please enter a whole number')
        pass

while True:
    user_input = input('Enter the labels of the lit indicators (Enter nothing to continue/skip): ')
    if user_input == '':
        break
    else:
        ind_lit.append()

while True:
    user_input = input('Enter the labels of the unlit indicators (Enter nothing to continue/skip): ')
    if user_input == '':
        break
    else:
        ind_unlit.append()

serial = input('Serial number: ').upper()
if (int(serial[-1]) % 2) == 0:
    serial_odd = False
else:
    serial_odd = True

vowels = set('aeiou')
serial_vowel = False
for vowel in vowels:
    if vowel in serial:
        serial_vowel = True

if input('Is there a parallel port? (Y/N)').lower() == 'y':
    port_parallel = True
else:
    port_parallel = False


bomb_data = {
    'bat_AA': aabatteries,
    'bat_B': bigbatteries,
    'bat_total': aabatteries+bigbatteries,
    'ind_LIT': ind_lit,
    'ind_UNLIT': ind_unlit,
    'serial': serial,
    'serial_odd': serial_odd,
    'serial_vowel': serial_vowel,
    'port_parallel': port_parallel,
}


while True:
    print('\n------------------------------------------')
    print('Keep Talking and Nobody Explodes Assistant')
    print('------------------------------------------\n')


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
    elif user_input == 'whos on first' or user_input == 'who\'s on first' or user_input == 'wof':
        whos_on_first()
    
    elif user_input == 'help':
        print('\n------OPTIONS------')
        print('Simple Wires, Button, Symbols, Memory')
        print('Password, Sequence, Complex Wires, Knob')
        print('Who\'s on first')
        print('-------------------')
    elif user_input == 'quit':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice!')