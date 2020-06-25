#Coded by Joshuahuahua
def password():
    
    word_dic = ['ABOUT', 'AFTER', 'AGAIN', 'BELOW', 'COULD', 'EVERY', 'FIRST', 'FOUND', 'GREAT', 'HOUSE', 'LARGE', 'LEARN', 'NEVER', 'OTHER', 'PLACE', 'PLANT', 'POINT', 'RIGHT', 'SMALL', 'SOUND', 'SPELL', 'STILL', 'STUDY', 'THEIR', 'THERE', 'THESE', 'THING', 'THINK', 'THREE', 'WATER', 'WHERE', 'WHICH', 'WORLD', 'WOULD', 'WRITE']

    slot_1 = input('Please input all letters in slot 1: ').upper()
    slot_2 = input('Please input all letters in slot 2: ').upper()
    slot_3 = input('Please input all letters in slot 3: ').upper()
    slot_4 = input('Please input all letters in slot 4: ').upper()

    for word in word_dic:
        if word[0] in slot_1 and word[1] in slot_2 and word[2] in slot_3 and word[3] in slot_4:
            print('The word is:', word)
            return
    print('---ERROR---\nWord not found!')