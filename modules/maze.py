maze_dic = [
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', 'O', '#'],
        ['#', ' ', '#', ' ', '#'],
        ['#', 'X', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#']
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', 'X', '#', 'O', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '*', ' ', '*', '#'],
        ['#', '#', '#', '#', '#']
    ],
    [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'O', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', 'X', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
]


def valid(maze, push):
    for j, row in enumerate(maze):
        for i, item in enumerate(maze[j]):
            if item == 'O':
                start_x = i
                start_y = j
                break
    
    x = start_x
    y = start_y
    for i, move in enumerate(push):
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1
    #print('x: ' + str(x) + '   y: ' + str(y))
    #print('value: ' + str(maze[y][x]))
    print(push)
    if maze[y][x] == '#':
        #print('NOT VALID')
        return False
    elif maze[y][x] == 'X':
        print('FOUND IT!')
        found = push.replace('UU', 'U').replace('DD', 'D').replace('LL', 'L').replace('RR', 'R')
        print(found)
        raise
    else:
        #print('VALID')
        return True



path = ['']
while True:
    #print()
    current = path.pop(0)
    for i in ['U', 'D', 'L', 'R']:
        #print(path)
        push = current + i
        #print('check ' + str(push))
        if valid(maze_dic[2], push):
            path.append(push)
            #path.append(push.replace('UD', '').replace('DU', '').replace('LR', '').replace('RL', ''))