
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
total_list = []
upper_list = []
ship_list = []
rounds = 0

for i in range(y):
    for t in range(x):
        total_list.append('*')

for i in range(y):
    if i == ((y + 1) // 2) - 1:
        ship_list.append('@')
    else:
        ship_list.append(' ')
for i in range(y):
    for t in range(g):
        total_list.append(' ')

control = True
while control == True:
    score = total_list.count(' ') - (g * y)
    #changing config
    if rounds % 5 == 0 and rounds > 0:
        control2 = True
        for i in range(y):
            if total_list[len(total_list) - i - 1] != ' ':
                control2 = False
        for i in range(y):
            if control2==True:
                total_list.pop()
                total_list.insert(0, ' ')
            else:
                control = False
                print('GAME OVER')
                break
    #win check
    if total_list.count('*') == 0:
        print('YOU WON!')
        control = False
    #board config
    for i in range(x + g):
        line_list = total_list[i * y:(i + 1) * y]
        for t in line_list:
            print(t, end='')
        print()

    for i in ship_list:
        print(i, end='')
    print()
    print(72*'-')
    if control== False:
        print('YOUR SCORE:',score)

    #taking command
    if control==True:
        command = input('Choose your action!\n').lower()

    #exit check
    if control==True:
        if command == 'exit':
            control = False
            for i in range(x + g):
                line_list = total_list[i * y:(i + 1) * y]
                for t in line_list:
                    print(t, end='')
                print()

            for i in ship_list:
                print(i, end='')
            print()
            print(72*'-')
            print('YOUR SCORE:',score)

    #round counter
    rounds += 1

    #right action
    if control==True:
        if command == 'right':
            if ship_list.index('@') == (y - 1):
                pass
            else:
                ship_list.pop()
                ship_list.insert(0, ' ')

    #left action
    if control==True:
        if command == 'left':
            if ship_list.index('@') == 0:
                pass
            else:
                ship_list.remove(' ')
                ship_list.append(' ')

    #fire action
    if control==True:
        if command == 'fire':
            location = ship_list.index('@')
            for m in range(len(total_list) - 1, -1, -1):
                if m % y == location and total_list[m] == ' ':
                    total_list.pop(m)
                    total_list.insert(m, '|')
                    for i in range(x + g):
                        line_list = total_list[i * y:(i + 1) * y]
                        for t in line_list:
                            print(t, end='')
                        print()

                    for i in ship_list:
                        print(i, end='')
                    print()
                    print(72*'-')
                    total_list.pop(m)
                    total_list.insert(m, ' ')
                elif m % y == location and total_list[m] == '*':
                    total_list.pop(m)
                    total_list.insert(m, ' ')
                    break

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
