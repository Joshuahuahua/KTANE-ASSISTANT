def solve_wires(red, white, blue, yellow, black):
    wires = red + white + blue + yellow + black
    if wires == 3:
        found = False
        if red == 0:
            print('Cut the second wire')
            found = True
        if not found and white > 0:
            if input('Is the white wire the last wire? (Y/N) > ').lower() == 'y':
                print('Cut the last wire')
                found = True
        if not found and blue > 1:
            print('Cut the last blue wire')
            found = True
        if not found:
            print('Cut the last wire')
            found = True
    if wires == 4:
        pass
    if wires == 5:
        pass
    if wires == 6:
        pass

