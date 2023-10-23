def hello():
    print("Приветствуем Вас в игре крестики нолики!")
    print("----------------------------------------")
    print("""Для хода указывайте сначала номер столбца
(по вертикали), а затем номер строки (по
горизонтали)""")
    print()

def printXO():
    print('    0   1   2')
    print('  '+'-'*13)
    for i, row in enumerate(data):
        print(i, *row, sep=' | ', end=' |\n')
        print('  '+'-'*13)
        
def cleardata():
    global data
    data = [['-']*3 for i in range(3)]

def checkwin():
    wincomb = (((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
               ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
               ((0,0), (1,1), (2,2)), ((2,0), (1,1), (0,2)))
    for comb in wincomb:
        a = data[comb[0][0]][comb[0][1]]
        b = data[comb[1][0]][comb[1][1]]
        c = data[comb[2][0]][comb[2][1]]
        if (data[comb[0][0]][comb[0][1]]==data[comb[1][0]][comb[1][1]]==data[comb[2][0]][comb[2][1]]) and a !='-':
            printXO()
            print('Выиграли', a)
            return 1

def nextgame():
    yn = input('Хотите начать новую игру? \n y/n?: ')
    if yn=='y':
        cleardata()
    else:
        global flag
        flag = False
        print('Прощайте!')

def checkxy():
    while True:
        strings = (input('Введите столбец и строку Вашего хода через пробел ').split())
        if len(strings)!=2:
            print('Координат должно быть 2!')
            continue
        y, x = strings
        if not(x.isdigit() and y.isdigit()):
            print('Введите числа!')
            continue
        y, x = list(map(int, strings))
        if not (x in moves and y in moves):
            print('Введите значение в диапазоне [0;2]')
            continue
        elif data[x][y] !='-':
            print('Данное поле уже занято!')
            continue
        break
    return y,x


hello()                
move = 0 # счетчик ходов
moves = (0,1,2) # проверка 
cleardata()
flag = True # играем пока не захотим прекратить
while flag:
    printXO()
    if move%2 == 0:
        print('Крестики ходят')
    else:
        print('Нолики ходят')
    y,x = checkxy()
    data[x][y]='X' if move%2==0 else 'O'
    move+=1
    if checkwin():
        nextgame()
    elif move==9:
        print('Ничья!')
        nextgame()

