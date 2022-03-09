def tictactoe():

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def welcome():

        greet = input("Hi, this is the first generation of tic tac toe made by NiceMan1337,\n"
                      "don't worry in next versions I will add something fresh.\n"
                      "To play you need a numeric keyboard (use numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9)\n"
                      "Start? (y/n): ")
        if greet == 'y':
            pass
        elif greet == 'n':
            exit()

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

    def occupied_num():

        if board[num] == player1 or player2:
            print('This number is now occupied!')
        elif board[num] == ' ':
            pass

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
        else:
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

        choose_site()
        draw(board)
        global num
        num = int(input('Player 1: Choose number to move (1-9): '))
        if num < 10:
            board[num] = player1
            draw(board)
        else:
            num = int(input('Player 1: Choose number to move (1-9): '))
            if num < 10:
                board[num] = player1
                draw(board)

    def secondmove():

        num = int(input('Player 2: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player2
                draw(board)
            else:
                occupied_num()
                num = int(input('Player 2: Choose number to move (1-9): '))
                board[num] = player2
                draw(board)
        else:
            num = int(input('Player 2: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player2
                    draw(board)
                else:
                    occupied_num()
                    num = int(input('Player 2: Choose number to move (1-9): '))
                    board[num] = player2
                    draw(board)

    def thirdmove():

        num = int(input('Player 1: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player1
                draw(board)
            else:
                occupied_num()
                num = int(input('Player 1: Choose number to move (1-9): '))
                board[num] = player1
                draw(board)
        else:
            num = int(input('Player 1: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player1
                    draw(board)
                else:
                    occupied_num()
                    num = int(input('Player 1: Choose number to move (1-9): '))
                    board[num] = player2
                    draw(board)

    def fourthmove():

        num = int(input('Player 2: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player2
                draw(board)
            else:
                occupied_num()
                num = int(input('Player 2: Choose number to move (1-9): '))
                board[num] = player2
                draw(board)
        else:
            num = int(input('Player 2: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player2
                    draw(board)
                else:
                    occupied_num()
                    num = int(input('Player 2: Choose number to move (1-9): '))
                    board[num] = player2
                    draw(board)

    def fifthmove():

        num = int(input('Player 1: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player1
                draw(board)
                winner()
            elif board[num] == 'X' or 'O':
                occupied_num()
                num = int(input('Player 1: Choose number to move (1-9): '))
                board[num] = player1
                draw(board)
                winner()
        else:
            num = int(input('Player 1: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player1
                    draw(board)
                    winner()
                else:
                    occupied_num()
                    num = int(input('Player 1: Choose number to move (1-9): '))
                    board[num] = player1
                    draw(board)
                    winner()

    def sixthmove():

        num = int(input('Player 2: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player2
                draw(board)
                winner()
            else:
                occupied_num()
                num = int(input('Player 2: Choose number to move (1-9): '))
                board[num] = player2
                winner()
                draw(board)
                winner()
        else:
            num = int(input('Player 2: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player2
                    draw(board)
                    winner()
                else:
                    occupied_num()
                    num = int(input('Player 2: Choose number to move (1-9): '))
                    board[num] = player2
                    draw(board)
                    winner()

    def seventhmove():

        num = int(input('Player 1: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player1
                draw(board)
                winner()
            else:
                occupied_num()
                num = int(input('Player 1: Choose number to move (1-9): '))
                board[num] = player1
                winner()
                draw(board)
                winner()
        else:
            num = int(input('Player 1: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player1
                    draw(board)
                    winner()
                else:
                    occupied_num()
                    num = int(input('Player 1: Choose number to move (1-9): '))
                    board[num] = player1
                    draw(board)
                    winner()

    def eighthmove():

        num = int(input('Player 2: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player2
                draw(board)
                winner()
            else:
                occupied_num()
                num = int(input('Player 2: Choose number to move (1-9): '))
                board[num] = player2
                winner()
                draw(board)
                winner()
        else:
            num = int(input('Player 2: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player2
                    draw(board)
                    winner()
                else:
                    occupied_num()
                    num = int(input('Player 2: Choose number to move (1-9): '))
                    board[num] = player2
                    draw(board)
                    winner()

    def ninethmove():

        num = int(input('Player 1: Choose number to move (1-9): '))
        if num < 10:
            if board[num] == ' ':
                board[num] = player1
                draw(board)
                winner()
            else:
                occupied_num()
                num = int(input('Player 1: Choose number to move (1-9): '))
                board[num] = player1
                winner()
                draw(board)
                winner()
        else:
            num = int(input('Player 1: Choose number to move (1-9): '))
            if num < 10:
                if board[num] == ' ':
                    board[num] = player1
                    draw(board)
                    winner()
                else:
                    occupied_num()
                    num = int(input('Player 1: Choose number to move (1-9): '))
                    board[num] = player1
                    draw(board)
                    winner()

    def winner():

        if player1 == board[1] and player1 == board[2] and player1 == board[3]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[1] and player2 == board[2] and player2 == board[3]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[4] and player1 == board[5] and player1 == board[6]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[4] and player2 == board[5] and player2 == board[6]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[7] and player1 == board[8] and player1 == board[9]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[7] and player2 == board[8] and player2 == board[9]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[1] and player1 == board[4] and player1 == board[7]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[1] and player2 == board[4] and player2 == board[7]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[2] and player1 == board[5] and player1 == board[8]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[2] and player2 == board[5] and player2 == board[8]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[3] and player1 == board[6] and player1 == board[9]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[3] and player2 == board[6] and player2 == board[9]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[1] and player1 == board[5] and player1 == board[9]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[1] and player1 == board[5] and player1 == board[9]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        elif player1 == board[3] and player1 == board[5] and player1 == board[7]:
            print('Player 1 wins! Thanks for playing!')
            exit()
        elif player2 == board[3] and player2 == board[5] and player2 == board[7]:
            print('Player 2 wins! Thanks for playing!')
            exit()
        else:
            pass

    def gameplay():

        firstmove()
        secondmove()
        thirdmove()
        fourthmove()
        fifthmove()
        sixthmove()
        seventhmove()
        eighthmove()
        ninethmove()

    welcome()
    gameplay()
tictactoe()
