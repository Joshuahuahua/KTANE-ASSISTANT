def maze():
    maze_dic = [
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
            ['#', '*', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '*', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '*', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', '*', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '*', '#', ' ', '#', '*', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '*', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', '*', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '*', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '*', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
            ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', '*', '#', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', '*', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', '*', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', '*', '#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ],
        [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '*', ' ', ' ', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', '*', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
    ]

    def valid(maze, push):
        for j, row in enumerate(maze):
            for i, item in enumerate(maze[j]):
                if item == 'O':
                    start_x = i
                    start_y = j
                    break # Attempt to assign start pos
        try:
            x = start_x
            y = start_y
        except UnboundLocalError:
            print('\n---ERROR---\nStart not found')
            return False

        for i, move in enumerate(push):
            if move == 'U':
                y-=1
            elif move == 'D':
                y+=1
            elif move == 'L':
                x-=1
            elif move == 'R':
                x+=1

        if maze[y][x] == '#': # Not a valid path
            return False
        elif maze[y][x] == 'X': # If end is found
            return 'Found'
        else: # Valid path
            return True



    maze_identifier = input('What are the coords for the 2 dots.\nUsage <XY, <XY>: ').replace(', ', ',').split(',')
    if len(maze_identifier) != 2:
        print('\n--ERROR--\nExpected 2 items!')
        return
    
    #Identify the maze
    found_maze = False
    for i, maze in enumerate(maze_dic):
        if maze[(int(maze_identifier[0][1])*2)-1][(int(maze_identifier[0][0])*2)-1] == '*' and maze[(int(maze_identifier[1][1])*2)-1][(int(maze_identifier[1][0])*2)-1] == '*':
            found_maze = i
    if len(str(found_maze)) != 1:
        print('\n---ERROR---\nMaze not found!')
        return
    
    #Set start and end points
    maze_info = input('What are the triangle and square\'s coords.\nUsage <triXY, <squXY>: ').replace(', ', ',').split(',')
    if len(maze_info) != 2:
        print('\n--ERROR--\nExpected 2 items!')
        return
    try:
        maze_dic[found_maze][(int(maze_info[0][1])*2)-1][(int(maze_info[0][0])*2)-1] = 'O'
        maze_dic[found_maze][(int(maze_info[1][1])*2)-1][(int(maze_info[1][0])*2)-1] = 'X'
    except:
        print('\n---ERROR---\nFailed to assign start and end points.')
    


    #Solve
    path = ['']
    try:
        while True:
            current = path.pop(0)
            for i in ['U', 'D', 'L', 'R']:
                push = current + i
                check = valid(maze_dic[found_maze], push) # Validate path
                if check == True:
                    if len(push) < 3:
                        path.append(push) # Append path
                    else:
                        # Filter out double-backs
                        if push[-1] == "L" and push[-2] != "R" or push[-1] == "R" and push[-2] != "L" or push[-1] == "U" and push[-2] != "D" or push[-1] == "D" and push[-2] != "U":
                            path.append(push)
                elif check == 'Found':
                    print('FOUND IT!')
                    found = push.replace('UU', 'U').replace('DD', 'D').replace('LL', 'L').replace('RR', 'R') # Rescale path
                    print(found)
                    return
    except IndexError:
        print('\n---ERROR---\nPath Not found')