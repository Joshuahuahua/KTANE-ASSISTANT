from modules.wires import wires
from modules.button import button
from wiresGUI import *

print("Keep Talking and Nobody Explodes Assistant\nThis CLI version is just to test some stuff\n")

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



user_input = input('Enter a module (Options: Wires, Button) > ').lower()
if user_input == 'wires':
    wiresGUI().start()
elif user_input == 'button':
    button(bomb_data)