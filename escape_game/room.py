rooms = {"room01" : [1, 0, 0, 0],
         "room02" : [1, 1, 0, 0], 
         "room03" : [1, 1, 0, 0],
         "room04" : [1, 1, 1, 1],
         "room05" : [0, 0, 1, 0],
         "room06" : [0, 0, 0, 1],
         "room07" : [1, 1, 0, 0],
         "room08" : [1, 1, 1, 1],
         "room09" : [0, 0, 1, 0],
         "room10" : [0, 0, 0, 1],
         "room11" : [0, 1, 0, 0]
         }



room_name = "room01"
dir = 0
running = True

def enter(room_name):
    print(f'현재 위치 : {room_name}')
    print("어디로 가시겠습니까?")
    print("1. 오른쪽\n2. 왼쪽\n3. 뒤쪽\n4. 앞쪽")
    direction = int(input())

    return direction

def move(room_name, walls, direction):
    nextRoom = room_name
    if room_name == "room01":
        if walls[direction - 1] == 1:
            nextRoom = 'room02'
            print(f'{nextRoom}으로 가볼까?')


        else:
            print('벽이야.')
    elif room_name == "room02":
        if walls[direction - 1] == 1:
            if direction -1 == 0:
                nextRoom = "room03"
                print(f'{nextRoom}으로 가볼까?')
    
            elif direction - 1 == 1:
                nextRoom = "room01"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room03":
        if walls[direction - 1] == 1:
            if direction -1 == 0:
                nextRoom = "room04"
                print(f'{nextRoom}으로 가볼까?')
    
            elif direction - 1 == 1:
                nextRoom = "room02"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room04":
        if walls[direction - 1] == 1:
            if direction -1 == 0:
                nextRoom = "room07"
                print(f'{nextRoom}으로 가볼까?')
            elif direction - 1 == 1:
                nextRoom = "room03"
                print(f'{nextRoom}으로 가볼까?')
            elif direction - 1 == 2:
                nextRoom = "room06"
                print(f'{nextRoom}으로 가볼까?')
            elif direction - 1 == 3:
                nextRoom = "room05"
                print(f'{nextRoom}으로 가볼까?')
        else:
            print('벽이야.')
    elif room_name == "room05":
        if walls[direction - 1] == 1:
            if direction -1 == 2:
                nextRoom = "room4"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room06":
        if walls[direction - 1] == 1:
            if direction -1 == 3:
                nextRoom = "room4"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room07":
        if walls[direction - 1] == 1:
            if direction -1 == 0:
                nextRoom = "room08"
                print(f'{nextRoom}으로 가볼까?')
    
            elif direction - 1 == 1:
                nextRoom = "room04"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room08":
        if walls[direction - 1] == 1:
            if direction -1 == 0:
                nextRoom = "room011"
                print(f'{nextRoom}으로 가볼까?')
            elif direction - 1 == 1:
                nextRoom = "room07"
                print(f'{nextRoom}으로 가볼까?')
            elif direction - 1 == 2:
                nextRoom = "room10"
                print(f'{nextRoom}으로 가볼까?')
            elif direction - 1 == 3:
                nextRoom = "room09"
                print(f'{nextRoom}으로 가볼까?')
        else:
            print('벽이야.')
    elif room_name == "room09":
        if walls[direction - 1] == 1:
            if direction -1 == 2:
                nextRoom = "room08"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room10":
        if walls[direction - 1] == 1:
            if direction -1 == 3:
                nextRoom = "room08"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')
    elif room_name == "room11":
        if walls[direction - 1] == 1:
            if direction -1 == 1:
                nextRoom = "room8"
                print(f'{nextRoom}으로 가볼까?')

        else:
            print('벽이야.')

    return nextRoom

while running:
    dir = enter(room_name)
    room_name = move(room_name, rooms[room_name], dir)