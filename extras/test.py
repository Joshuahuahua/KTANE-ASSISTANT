### test file ###






x = ['FRK', 'BOB']
y = ['TRN', 'IND']



print(str(x+y))








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