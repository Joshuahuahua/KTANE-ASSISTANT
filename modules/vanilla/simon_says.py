def simon_says(bomb_data, strikes, user_input):
    
    vowel = {
    'red': ['blue', 'yellow', 'green'],
    'blue': ['red', 'green', 'red'],
    'green': ['yellow', 'blue', 'yellow'],
    'yellow': ['green', 'red', 'blue']
    }

    non_vowel = {
    'red': ['blue', 'red', 'yellow'],
    'blue': ['yellow', 'blue', 'green'],
    'green': ['green', 'yellow', 'blue'],
    'yellow': ['red', 'green', 'red']
    }

    memory = []

    while True:
        try:
            #strikes = int(input('Enter number of strikes (0, 1 or 2): ').lower())
            strikes = int(strikes).lower()
            if strikes > -1 and strikes < 3:
                break
            else:
                continue
        except ValueError:
            pass

    while True:
        try:
            #user_input = input('Usage <color> / <(s) edit strikes> / <(e)xit>: ').lower()
            user_input = user_input.lower()
            if user_input == 'e' or user_input == 'exit':
                break
            elif user_input == 's' or user_input == 'strikes':
                memory = []
                while True:
                        try:
                            #strikes = int(input('Enter number of strikes (0, 1 or 2): ').lower())
                            strikes = int(strikes).lower()
                            if strikes > -1 and strikes < 3:
                                break
                            else:
                                continue
                        except ValueError:
                            pass 
            elif bomb_data['serial_vowel']:
                memory.append(vowel[user_input][strikes])
                print('------- INPUT IN FOLLOWING ORDER -------')
                for color in memory:
                    print(color)
            else:
                memory.append(non_vowel[user_input][strikes])
                print('------- INPUT IN FOLLOWING ORDER -------')
                for color in memory:
                    print(color)
        except KeyError:
            pass