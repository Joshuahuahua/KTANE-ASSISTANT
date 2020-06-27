#Coded by Joshuahuahua
def emoji_math():
    emoji_dic = [
    {'symbol': ':)', 'value': '0'},
    {'symbol': '=(', 'value': '1'},
    {'symbol': '(:', 'value': '2'},
    {'symbol': ')=', 'value': '3'},
    {'symbol': ':(', 'value': '4'},
    {'symbol': '):', 'value': '5'},
    {'symbol': '=)', 'value': '6'},
    {'symbol': '(=', 'value': '7'},
    {'symbol': ':|', 'value': '8'},
    {'symbol': '|:', 'value': '9'}]

    expression = input('Input the expression on the bomb: ')
    try:
        for term in emoji_dic:
            expression = expression.replace(term['symbol'], term['value'])

        if expression.count('+') == 1:
            result = int(expression.split('+')[0]) + int(expression.split('+')[1])
        elif expression.count('-') == 1:
            result = int(expression.split('-')[0]) - int(expression.split('-')[1])
        print('The answer is:', result)
    except:
        print('\n---ERROR---\nInvalid Input')

emoji_math()