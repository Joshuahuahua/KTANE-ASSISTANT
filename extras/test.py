### test file ###





key_dic = [
    {'condition': '', 'symbols': ['flat'], 'required': 'Even', 'sequence': 'Bb Bb Bb Bb Gb Ab Bb Ab Bb'},
    {'condition': 'OR', 'symbols': ['common time', 'sharp'], 'required': 'H2', 'sequence': 'Eb Eb D D Eb Eb D Eb Eb D D Eb'},
    {'condition': 'AND', 'symbols': ['natural', 'fermata'], 'required': '', 'sequence': 'E F# F# F# E E E'},
    {'condition': 'OR', 'symbols': ['cut time', 'turn'], 'required': 'RCA', 'sequence': 'Bb A Bb F Eb Bb A Bb F Eb'},
    {'condition': '', 'symbols': ['clef'], 'required': 'SND', 'sequence': 'E E E C E G G'},
    {'condition': 'OR', 'symbols': ['mordent', 'fermata', 'common time'], 'required': 'B3', 'sequence': 'C# D E F C# D E F Bb A'},
    {'condition': 'AND', 'symbols': ['flat', 'sharp'], 'required': '', 'sequence': 'G G C G G C G C'},
    {'condition': 'OR', 'symbols': ['cut time', 'mordent'], 'required': 'S378', 'sequence': 'A E F G F E D D F A'},
    {'condition': 'OR', 'symbols': ['Natural', 'Turn', 'Clef'], 'required': '', 'sequence': 'G G G Eb Bb G Eb Bb G'},
    {'condition': 'NO', 'symbols': [''], 'required': '', 'sequence': 'B D A G A B D A'}]

for i, key in enumerate(key_dic):
    arr = key['sequence'].split(' ')
    ret = ''
    for let in arr:
        ret = ret + let + ', '
    key_dic[i]['sequence'] = ret
    print(key_dic[i])





'''

def isnotable(checkName):
    return 'Is notable' if checkName[0].lower() == 'n' and len(checkName) >= 5 else 'Is NOT notable'
print(isnotable(input('Input a nickname: ')))


'''





'''
translate_dic = [
    {'value': 0, 'note': 'C'},
    {'value': 1, 'note': 'C#'},
    {'value': 2, 'note': 'D'},
    {'value': 3, 'note': 'D#'},
    {'value': 4, 'note': 'E'},
    {'value': 5, 'note': 'F'},
    {'value': 6, 'note': 'F#'},
    {'value': 7, 'note': 'G'},
    {'value': 8, 'note': 'G#'},
    {'value': 9, 'note': 'A'},
    {'value': 10, 'note': 'A#'},
    {'value': 11, 'note': 'B'}
]

symbols_input = input('Usage <symbol1, symbol2...symbol4>: ').upperC, C#, D^S().replace(', ', ',').split(',')
print(symbols_input)
for note in translate_dic:
    symbols_input = symbols_input.replace(note['note'], note['value'])
print(symbols_input)



def transform(mode, sequence):
    for i, method in enumerate(mode):
        if method == 'R':
            sequence.reverse()
        elif method == 'T':
            sequence = list((x+mode[i+1]) % 12 for x in sequence)
        elif method == 'I':
            newList = sequence
            for i in range(0,len(sequence)-1):
                tempList = []
                diff = sequence[i]-sequence[i+1]
                for item in newList[:i+1]:
                    tempList.append(item)
                for x in range(0, len(newList[i+1:])):
                    tempList.append(newList[i:][x]+diff)
                newList = tempList
            sequence = list(x % 12 for x in tempList)
    return sequence


mode = ['I']
sequence = [5,6,7,6,5]
output = transform(mode, sequence)
print(output)

translate_dic = [
    {'value': 0, 'note': 'C'},
    {'value': 1, 'note': 'C#'},
    {'value': 2, 'note': 'D'},
    {'value': 3, 'note': 'D#'},
    {'value': 4, 'note': 'E'},
    {'value': 5, 'note': 'F'},
    {'value': 6, 'note': 'F#'},
    {'value': 7, 'note': 'G'},
    {'value': 8, 'note': 'G#'},
    {'value': 9, 'note': 'A'},
    {'value': 10, 'note': 'A#'},
    {'value': 11, 'note': 'B'}
]
for i, current_input in enumerate(output):
    for note in translate_dic:
        if current_input == note['value']:
            output[i] = note['note']
print(output)


'''

'''


def wrap(x, xmin, xmax):
    while not xmax >= x >= xmin:
        x = x+xmax if x < xmin else x-xmax
    return x


print(wrap(10, 0, 9))
print([x % 10])
'''
'''

x = ['FRK', 'BOB']
y = ['TRN', 'IND']



print(str(x+y))


'''





'''

a = 1
b = 1
c = 2
x = 0
y = 1
z = 0

print([a,b,c,x,y,z].sort())
'''

'''
test = sum([1 for num in [a,b,c,x,y,z] if num > 0])
test = sum([1 for x in [bomb_data['port_parallel'],bomb_data['port_dvi'],bomb_data['port_ps2'],bomb_data['port_rj45'],bomb_data['port_serial'],bomb_data['port_rca']] if x > 0])



#print(test)
if test > 3:
    print('yes')
else:
    print('no')


'''


'''
test = 1
print(int(str(test)[-1]))
print(int(str(test)[-1])+1)

test = 'aaaaa9j4j3j83'

print(list(x for x in test if x.isdigit())[0])


'''

'''

bomb_data = {
    'bat_AA': 0,
    'bat_B': 0,
    'bat_total': 0,
    'ind_LIT': ['IND', 'NSA'],
    'ind_UNLIT': ['CLR'],
    'serial': '0Z3ZJ6',
    'serial_odd': False,
    'serial_vowel': False,
    'port_parallel': False,
    'port_dvi': True,
    'port_ps2': False,
    'port_rj45': True,
    'port_serial': False,
    'port_rca': True,
    'modules_total': 101,
    'modules_solved': 0,
}



if [bomb_data['port_parallel'], bomb_data['port_dvi'], bomb_data['port_ps2'], bomb_data['port_rj45'], bomb_data['port_serial'], bomb_data['port_rca']].count(True) < 3:
    print('yes')
else:
    print('no')

'''







'''

x = 'h311o'
y = [1, 2, 3, 4, 5, 6]

z = sum(1-n%2 for n in y)

#print(z)


print(len(list(num for num in x if num.isdigit() and int(num) %2 == 0)))
print(len(list(num for num in x if num.isdigit() and int(num) %2 != 0)))

if len(list(num for num in x if num.isdigit() and int(num) %2 == 0)) > len(list(num for num in x if num.isdigit() and int(num) %2 != 0)):
    print('even')
else:
    print('odd')



z = list(int(num) for num in x if num.isdigit())
z.sort(reverse=True)
print('hello'*z[0])

'''