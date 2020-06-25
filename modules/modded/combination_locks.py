#Coded by Joshuahuahua
def combination_locks(bomb_data):
    code_1 = wrap(int(bomb_data['serial'][-1])+bomb_data['modules_solved']+bomb_data['bat_total'])
    code_2 = wrap(bomb_data['modules_total']+bomb_data['modules_solved'])
    code_3 = wrap(code_1+code_2)
    print('Right:', code_1, '\nLeft:', code_2, '\nRight:', code_3)
def wrap(x):
    while x > 19: x-=20
    return x