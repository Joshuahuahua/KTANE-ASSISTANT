#Coded by Matthew Alphonso
def two_bits(bomb_data):
    
    dic = {
    '00': 'KB','01': 'DK', '02': 'GV', '03': 'TK', '04': 'PV', '05': 'KP', '06': 'BV', '07': 'VT', '08': 'PZ', '09': 'DT',
    '10': 'EE','11': 'ZK', '12': 'KE', '13': 'CK', '14': 'ZP', '15': 'PP', '16': 'TP', '17': 'TG', '18': 'PD', '19': 'PT',
    '20': 'TZ','21': 'EB', '22': 'EC', '23': 'CC', '24': 'CZ', '25': 'ZV', '26': 'CV', '27': 'GC', '28': 'BT', '29': 'GT',
    '30': 'BZ','31': 'PK', '32': 'KZ', '33': 'KG', '34': 'VD', '35': 'CE', '36': 'VB', '37': 'KD', '38': 'GG', '39': 'DG',
    '40': 'PB','41': 'VV', '42': 'GE', '43': 'KV', '44': 'DZ', '45': 'PE', '46': 'DB', '47': 'CD', '48': 'TD', '49': 'CB',
    '50': 'GB','51': 'TV', '52': 'KK', '53': 'BG', '54': 'BP', '55': 'VP', '56': 'EP', '57': 'TT', '58': 'ED', '59': 'ZG',
    '60': 'DE','61': 'DD', '62': 'EV', '63': 'TE', '64': 'ZD', '65': 'BB', '66': 'PC', '67': 'BD', '68': 'KC', '69': 'ZB',
    '70': 'EG','71': 'BC', '72': 'TC', '73': 'ZE', '74': 'ZC', '75': 'GP', '76': 'ET', '77': 'VC', '78': 'TB', '79': 'VZ',
    '80': 'EZ','81': 'EK', '82': 'DV', '83': 'CG', '84': 'VE', '85': 'DP', '86': 'BK', '87': 'PG', '88': 'GK', '89': 'GZ',
    '90': 'KT','91': 'CT', '92': 'ZZ', '93': 'VG', '94': 'GD', '95': 'CP', '96': 'BE', '97': 'ZT', '98': 'VK', '99': 'DC'}

    alphabet_numeric = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8','i': '9',
        'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17',
        'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
    }

    for x in bomb_data['serial'].lower():
        if x.isalpha():
            first_letter_pos = int(alphabet_numeric[x])
            break
        else:
            first_letter_pos = 0

    for x in bomb_data['serial']:
        if x.isdigit():
            last_digit = int(x)

    code_1 = first_letter_pos + last_digit * bomb_data['bat_total']

    if bomb_data['port_rca'] == True and bomb_data['port_rj45'] == False:
        code_1*=2
    if code_1 > 99:
        code_1 = str(code_1[2:])
    elif code_1 < 10:
        code_1 = '0' + str(code_1)
    print('First code -', dic[str(code_1)], '\nPress "QUERY"')
    
    while True:
        code_2 = input('\nWhat is the code:')
        try:
            if code_2.isdigit():
                print('Second code -', dic[str(code_2)], '\nPress "QUERY"')
                break
            else:
                raise
        except:
            print('Invalid key')
    
    while True:
        code_3 = input('\nWhat is the code:')
        try:
            if code_3.isdigit():
                print('Third code -', dic[str(code_3)], '\nPress "QUERY"')
                break
            else:
                raise
        except:
            print('Invalid key')
    
    while True:
        code_4 = input('\nWhat is the code:')
        try:
            if code_4.isdigit():
                print('Fourth code -', dic[str(code_4)], '\nPress "SUBMIT"')
                break
            else:
                raise
        except:
            print('Invalid key')