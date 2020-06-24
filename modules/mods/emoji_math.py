#emoji_math fucntion - Devvvv-WB work

#Numbers:

# :) = 0
# =( = 1
# (: = 2
# )= = 3
# :( = 4
# ): = 5
# =) = 6
# (= = 7
# :| = 8
# |: = 9

#Diable function and remove comments on value1 and value2 to test code. Also update indents
def emoji_math(value1, value2):
    

    #print("Characters:\n:)\n=(\n(:\n)=\n:(\n):\n=)\n(=\n(=\n:|\n|:")


    while True:
        #value1 = input("Enter first characters: ")
        if value1 == ':)':
            x = 0
        elif value1 == '=(':
            x = 1
        elif value1 == '(:':
            x = 2
        elif value1 == ')=':
            x = 3
        elif value1 == ':(':
            x = 4
        elif value1 == '):':
            x = 5
        elif value1 == '=)':
            x = 6
        elif value1 == '(=':
            x = 7
        elif value1 == ':|':
            x = 8
        elif value1 == '|:':
            x = 9
        else:
            print("Invalid entry")
            continue

        neg1 = input('Is this value a negative (Y/N)?: ')
        if neg1 == 'Y':
            x = x * -1
            break
        elif neg1 == 'N':
            break
        else:
            print("Invalid input")
            continue
    
    while True:
        #value2 = input("Enter second characters: ")
        if value2 == ':)':
            y = 0
        elif value2 == '=(':
            y = 1
        elif value2 == '(:':
            y = 2
        elif value2 == ')=':
            y = 3
        elif value2 == ':(':
            y = 4
        elif value2 == '):':
            y = 5
        elif value2 == '=)':
            y = 6
        elif value2 == '(=':
            y = 7
        elif value2 == ':|':
            y = 8
        elif value2 == '|:':
            y = 9
        else:
            print("Invalid entry")
            continue

        neg2 = input('Is this value a negative (Y/N)?: ')
        if neg2 == 'Y':
            y = y * -1
            break
        elif neg2 == 'N':
            break
        else:
            print('Invalid input')
            continue

    result = x + y
    print('Result:', result)