from modules.wires import solve_wires

print("Keep Talking and Nobody Explodes Assistant\nThis CLI version is just to test some stuff\n")

user_input = input('Enter a module (Options: Wires) > ').lower()

if user_input == "wires":
    colors = ['red', 'white', 'blue', 'yellow', 'black']
    color_dict = {}
    for color in colors:
        color_dict[color] = int(input('How many ' + color + ' wires? > '))
    solve_wires(color_dict['red'], color_dict['white'], color_dict['blue'], color_dict['yellow'], color_dict['black'])