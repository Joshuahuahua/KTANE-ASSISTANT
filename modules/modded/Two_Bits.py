def two_bits(bomb_data):
    
    test = [
    {'00': 'kb','01': 'dk', '02': 'gv', '03': 'tk', '04': 'pv', '05': 'kp', '06': 'bv', '07': 'vt', '08': 'pz', '09': 'dt',
    '10': 'ee','11': 'zk', '12': 'ke', '13': 'ck', '14': 'zp', '15': 'pp', '16': 'tp', '17': 'tg', '18': 'pd', '19': 'pt',
    '20': 'tz','21': 'eb', '22': 'ec', '23': 'cc', '24': 'cz', '25': 'zv', '26': 'cv', '27': 'gc', '28': 'bt', '29': 'gt',
    '30': 'bz','31': 'pk', '32': 'kz', '33': 'kg', '34': 'vd', '35': 'ce', '36': 'vb', '37': 'kd', '38': 'gg', '39': 'dg',
    '40': 'pb','41': 'vv', '42': 'ge', '43': 'kv', '44': 'dz', '45': 'pe', '46': 'db', '47': 'cd', '48': 'td', '49': 'cb',
    '50': 'gb','51': 'tv', '52': 'kk', '53': 'bg', '54': 'bp', '55': 'vp', '56': 'ep', '57': 'tt', '58': 'ed', '59': 'zg',
    '60': 'de','61': 'dd', '62': 'ev', '63': 'te', '64': 'zd', '65': 'bb', '66': 'pc', '67': 'bd', '68': 'kc', '69': 'zb',
    '70': 'eg','71': 'bc', '72': 'tc', '73': 'ze', '74': 'zc', '75': 'gp', '76': 'et', '77': 'vc', '78': 'tb', '79': 'vz',
    '80': 'ez','81': 'ek', '82': 'dv', '83': 'cg', '84': 've', '85': 'dp', '86': 'bk', '87': 'pg', '88': 'gk', '89': 'gz',
    '90': 'kt','91': 'ct', '92': 'zz', '93': 'vg', '94': 'gd', '95': 'cp', '96': 'be', '97': 'zt', '98': 'vk', '99': 'dc'}
    ]

    alphabet_numeric = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26'
    }


    bomb_data = {
        'bat_total': 3, 
        'serial': '4L5QF2', 
        'port_rca': True, 
        'port_rj45': False
    } # <--- Testing purposes
    
    
    for x in bomb_data['serial'].lower():
        if x.isalpha():
            first_letter_pos = alphabet_numeric[x]
            break
        else:
            first_letter_pos = 0
    for x in bomb_data['serial']:
        if x.isdigit():
            last_digit = int(x)
    current_code = last_digit*bomb_data['bat_total']
    if bomb_data['port_rca'] == True and bomb_data['port_rj45'] == False:
        current_code = int(current_code)*2
        current_code = str(current_code)
        print('First code -',test[0][current_code])
        print('"Query"')
    
    while True:
        code2 = input('\nWhat is the code:')
        try:
            if code2.isdigit():
                print('Second code -',test[0][code2])
                print('"Query"')
            elif any(code2.isalnum()) or code2.isspace() or code2 == '' :
                print('Invalid key')
        except:
            print('Invalid key')
        break
    while True:
        code3 = input('\nWhat is the code:')
        try:
            if code3.isdigit():
                print('Third code -',test[0][code3])
                print('"Query"')
            elif any(code3.isalnum()) or code3.isspace() or code3 == '' :
                print('Invalid key')
        except:
            print('Invalid key')
        break
    while True:
        code4 = input('\nWhat is the code:')
        try:
            if code4.isdigit():
                print('Final code -',test[0][code4])
                print('"Summit"')
            elif any(code4.isalnum()) or code4.isspace() or code4 == '' :
                print('Invalid key')
        except:
            print('Invalid key')
        break
