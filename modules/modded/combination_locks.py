#made by Matthew Alphonso
def combination_locks():
    while True:
    factor_codes = input('\nhow many factor codes are there?')
    if factor_codes == '2':
        while True:
            factor_code1 = input('\nWhat is the first factor code?')
            if factor_code1.isdigit():
                factor_code1_str_list = list(factor_code1)
                factor_code1_list = []
                for x in factor_code1_str_list:
                    factor_code1  = int(x)
                    factor_code1_list.append(factor_code1)
                while True:
                    factor_code2 = input('\nWhat is the second factor code?')
                    if factor_code2.isdigit():
                        factor_code2_list = []
                        factor_code2_str_list = list(factor_code2)
                        for x in factor_code2_str_list:
                            factor_code2  = int(x)
                            factor_code2_list.append(factor_code2)
                            first_number = min(factor_code1_list) + min(factor_code2_list)
                            first_number = bomb_data['bat_total'] + first_number 
                            if first_number > 19:
                                first_number = first_number - 19 
                            second_number = max(factor_code1_list) + max(factor_code2_list)
                        while True:
                            modules_solved = input('\nhow many modules have you solved?')
                            if modules_solved.isdigit():
                                modules_solved = int(modules_solved)
                                second_number = second_number + modules_solved
                                if second_number > 19:
                                    second_number = second_number - 20
                                third_number = first_number + second_number
                                if third_number > 19:
                                    third_number = third_number - 20
                                print('\nFist number:',first_number,'\nSecond number',second_number,'\nThird number',third_number)
                            
                            else:
                                print('Invalid Number')
                            break
                    break
            else:
                print('Invalid Number')
            break

    elif factor_codes.isdigit():
        while True:
            modules_solved = input('\nhow many modules have you solved?')
            if modules_solved.isdigit():
                modules_solved = int(modules_solved)
                for x in bomb_data['serial']:
                    if x.isdigit():
                        last_digit = int(x)
                first_number = modules_solved + last_digit
                first_number = bomb_data['bat_total'] + first_number 
                if first_number > 19:
                    first_number = first_number - 19 
                while True:
                    total_modules = input('\nHow many modules are there(include needy modules)')
                    if total_modules.isdigit():
                        total_modules = int(total_modules)
                        second_number = total_modules + modules_solved
                        third_number = first_number + second_number
                        if third_number > 19:
                            third_number = third_number - 20
                        print('\nFist number:',first_number,'\nSecond number',second_number,'\nThird number',third_number)
                        break
                    else:
                        print('invalid Number')
                    break
            else:
                print('invalid Number')
            break    
    else:
        print('Inalid Number')
        
    break

bomb_data = {
    'bat_total': 3, 
    'serial': '4L5Q5F', 
    'port_rca': True, 
    'port_rj45': False
} # <--- Testing purposes
combination_locks(bomb_data)
    
