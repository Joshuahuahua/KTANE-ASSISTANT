from modules.wires import wires

print("Keep Talking and Nobody Explodes Assistant\nThis CLI version is just to test some stuff\n")

bomb_data = {
    'test': 0,
    'test2': 'string',
    'test3': True
} 

user_input = input('Enter a module (Options: Wires) > ').lower()




wires(bomb_data)