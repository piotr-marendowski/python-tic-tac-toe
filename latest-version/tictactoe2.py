def tictactoe():

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def welcome():

        greet = input("Hi, this is the tic tac toe game made by NiceMan1337,\n"
                      "To play you need a numeric keyboard (use numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9)\n"
                      "Start? (y/n): ")
        if greet == 'y':
            pass
        else:
            exit()

    def choose_site():

        global player1
        global player2
        marker = input('Choose site for player 1 (X or O): ').upper()
        if marker == 'X':
            player1 = 'X'
            player2 = 'O'
            print("Player 1 is 'X' player 2 is 'O'.")
        elif marker == 'O':
            player1 = 'O'
            player2 = 'X'
            print("Player 1 is 'O' player 2 is 'X'.")
        elif marker != 'X' or 'O':
            player1 = 'X'
            player2 = 'O'
            print("Player 1 is 'X' player 2 is 'O'.")

    def firstmove():

        welcome()
        choose_site()
        draw(board)
        global num
        global loop
        while True:
            try:
                num = int(input('Player 1: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    board[num] = player1
                    draw(board)
                break
            except ValueError:
                print("Only numbers allowed!")

    def secondmove():

        while True:
            try:
                num = int(input('Player 2: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player2
                        draw(board)
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 2: Choose number to move (1-9): '))
                        board[num] = player2
                        draw(board)
                break
            except ValueError:
                print("Only numbers allowed!")

    def thirdmove():

        while True:
            try:
                num = int(input('Player 1: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player1
                        draw(board)
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 1: Choose number to move (1-9): '))
                        board[num] = player1
                        draw(board)
                break
            except ValueError:
                print("Only numbers allowed!")

    def fourthmove():

        while True:
            try:
                num = int(input('Player 2: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player2
                        draw(board)
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 2: Choose number to move (1-9): '))
                        board[num] = player2
                        draw(board)
                break
            except ValueError:
                print("Only numbers allowed!")

    def fifthmove():

        while True:
            try:
                num = int(input('Player 1: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player1
                        draw(board)
                        winner()
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 1: Choose number to move (1-9): '))
                        board[num] = player1
                        draw(board)
                        winner()
                break
            except ValueError:
                print("Only numbers allowed!")

    def sixthmove():

        while True:
            try:
                num = int(input('Player 2: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player2
                        draw(board)
                        winner()
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 2: Choose number to move (1-9): '))
                        board[num] = player2
                        draw(board)
                        winner()
                break
            except ValueError:
                print("Only numbers allowed!")

    def seventhmove():

        while True:
            try:
                num = int(input('Player 1: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player1
                        draw(board)
                        winner()
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 1: Choose number to move (1-9): '))
                        board[num] = player1
                        draw(board)
                        winner()
                break
            except ValueError:
                print("Only numbers allowed!")

    def eighthmove():

        while True:
            try:
                num = int(input('Player 2: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player2
                        draw(board)
                        winner()
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 2: Choose number to move (1-9): '))
                        board[num] = player2
                        draw(board)
                        winner()
                break
            except ValueError:
                print("Only numbers allowed!")

    def ninethmove():

        while True:
            try:
                num = int(input('Player 2: Choose number to move (1-9): '))
                if num < 10:
                    loop = True
                else:
                    loop = False
                if loop:
                    if board[num] == ' ':
                        board[num] = player2
                        draw(board)
                        winner()
                        if win != player1 or player2:
                            print("Draw! No one wins!")
                            exit()
                    else:
                        print("This number is occupied!")
                        num = int(input('Player 2: Choose number to move (1-9): '))
                        board[num] = player2
                        draw(board)
                        winner()
                        if win != player1 or player2:
                            print("Draw! No one wins!")
                            exit()
                break
            except ValueError:
                print("Only numbers allowed!")

    def draw(board):

        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '  ' + board[0])
        print('   |   |')
        print('---+---+---')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('---+---+---')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def winner():

        global win
        if player1 == board[1] and player1 == board[2] and player1 == board[3]:
            win = player1
        elif player2 == board[1] and player2 == board[2] and player2 == board[3]:
            win = player2
        elif player1 == board[4] and player1 == board[5] and player1 == board[6]:
            win = player1
        elif player2 == board[4] and player2 == board[5] and player2 == board[6]:
            win = player2
        elif player1 == board[7] and player1 == board[8] and player1 == board[9]:
            win = player1
        elif player2 == board[7] and player2 == board[8] and player2 == board[9]:
            win = player2
        elif player1 == board[1] and player1 == board[4] and player1 == board[7]:
            win = player1
        elif player2 == board[1] and player2 == board[4] and player2 == board[7]:
            win = player2
        elif player1 == board[2] and player1 == board[5] and player1 == board[8]:
            win = player1
        elif player2 == board[2] and player2 == board[5] and player2 == board[8]:
            win = player2
        elif player1 == board[3] and player1 == board[6] and player1 == board[9]:
            win = player1
        elif player2 == board[3] and player2 == board[6] and player2 == board[9]:
            win = player2
        elif player1 == board[1] and player1 == board[5] and player1 == board[9]:
            win = player1
        elif player2 == board[1] and player1 == board[5] and player1 == board[9]:
            win = player2
        elif player1 == board[3] and player1 == board[5] and player1 == board[7]:
            win = player1
        elif player2 == board[3] and player2 == board[5] and player2 == board[7]:
            win = player2
        else:
            win = ""

        if win == player1:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif win == player2:
            print('Player 2 wins! Thanks for playing!')
            exit()

    firstmove()
    secondmove()
    thirdmove()
    fourthmove()
    fifthmove()
    sixthmove()
    seventhmove()
    eighthmove()
    ninethmove()
tictactoe()
