import random
print('\n\n')
print('========================================================================================================================')
print('-------XO-XO-XO-XO-XO-XO-XO-XO-XO-------            TIC TAK TOE          ----------XO-XO-XO-XO-XO-XO-XO-XO-XO-XO--------')
print('========================================================================================================================')
print('\n')
print('  WELCOME ABOARD AMIGO!\n  Lets get familiar with the game format, shall we??\n     ')


theboard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',  # board format
            '7': ' ', '8': ' ', '9': ' '}


def pboard(board):
    print('    '+board['1'] + '1| ' + board['2'] + '2| ' + board['3'] + '3')
    print("    --+---+---")
    print('    '+board['4'] + '4| ' + board['5'] + '5| ' + board['6'] + '6')
    print("    --+---+---")
    print('    '+board['7'] + '7| ' + board['8'] + '8| ' + board['9'] + '9')


print("\n **   The format of the board is as follows:\n")
pboard(theboard)
print('\n**    enter the no. of the box u chose to mark in\n')

print('\n              ------------------------------\n              |        MAIN  MENU          |\n              ------------------------------\n\n\n')
print('    INSTRUCTIONS:\n\n1. To PLAY the game enter "P" ')
print('2. To EXIT without playing enter "Q"')
print('3. To see the SCORE BOARD now enter "S" \n\n')
mode=input('enter your choice (P/Q/S) : ')

if mode.upper()=='P':


 '''import mysql.connector as ms

user='root'
password='1414'
host='localhost'
db='tiktak'

con=ms.connect(host='localhost',user='root',password='1414',db='tiktak')

if con.is_connected():
    print('connected')'''

theboard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',  # board format
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []
for key in theboard:
    board_keys.append(key)


# def menu
def plr_name():  # GIVEN TWO CONDITIONS, IF ONE PLAYER IS CHOSEN, SECOND NAME WON'T BE ASKED
    if x == 1:
        a = input("enter the player name:")
        if a == '' or a == ' ':
            print("This name is not defined")
            plr_name()
        else:
            print('Accepted')

    elif x == 2:
        a = input("enter 1st player name:")
        if a == '' or a == ' ':
            print("This name is not defined")
            plr_name()

        print("accepted \n")

        b = input("enter 2nd player: ")
        if b == '' or b == ' ':
            print('not defined.....\n enter again')
            plr_name()
        else:
            print("accepted")



g = 0


def enter():
    global x
    x = int(input("enter the no of players \n (1,2): "))
    if x == 1 or x == 2:  # for x==1,import random for the single playeer mode
        print("kindly enter the details: \n")
        plr_name()
        global g
        g = x

    else:
        print("its not a valid no.! please enter again \n")
        print('')
        enter()


enter()

'''if g==x:
    if g == 1 or g == 2:
        def pboard(board):
            print(board['1'] + '1| ' + board['2'] + '2| ' + board['3'] + '3')
            print("--+---+---")
            print(board['4'] + '4| ' + board['5'] + '5| ' + board['6'] + '6')
            print("--+---+---")
            print(board['7'] + '7| ' + board['8'] + '8| ' + board['9'] + '9')'''




    # printing the board format for the user to get familiar


def printboard(board):
    print('        '+board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print("        --+---+---")
    print('        '+board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print("        --+---+---")
    print('        '+board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


# printboard(theboard)


# ask the user what the want to choose i.e. either 'X' or 'O'
if x == 2:
    def game():
        sym = {}
        key = 'player1'
        val = str(input('choose symbol......\n Player1 choose your symbol...: (X/O)'))
        sym[key] = val
        if val.upper() == 'X':
            sym['player2'] = 'O'
            print('player 2 gets O\n')
            print('\n PLAYER-1 goes first.........BEST OF LUCK TO BOTH OF YOU  :D')
        else:
            sym['player2'] = 'X'
            print('player 2 gets X\n')
            print('\n PLAYER-2 goes first.........BEST OF LUCK TO BOTH OF YOU  :D')
            pass

        turn = 'X'
        count = 0

        for i in range(10):
            printboard(theboard)
            print("It's", turn, "'s turn, move to where?")
            move = input()
            print(' ')

            if theboard[move] == ' ':
                theboard[move] = turn
                count += 1
            else:
                print("The place is already filled, Please move elsewhere..")
                continue
            if count >= 5:
                if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                    printboard(theboard)
                    print("Game Over.")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D  --------X--------X-------X--------- ")
                    break
                elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                    printboard(theboard)
                    print("Game over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D   --------X--------X-------X--------- ")
                    break
                elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                    printboard(theboard)
                    print("Game Over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D   --------X--------X-------X--------- ")
                    break
                elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                    printboard(theboard)
                    print("Game Over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D   --------X--------X-------X--------- ")
                    break
                elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                    printboard(theboard)
                    print("Game Over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D   --------X--------X-------X--------- ")
                    break
                elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                    printboard(theboard)
                    print("Game Over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D   --------X--------X-------X--------- ")
                    break
                elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                    printboard(theboard)
                    print("Game Over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D   --------X--------X-------X--------- ")
                    break
                elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                    printboard(theboard)
                    print("Game Over. ")
                    print("   ------X-------X----------X----   ", turn,
                          "Won the match! :D    --------X--------X-------X--------- ")
                    break
            if count == 9:
                print("Game Over. ")
                print("-----X-------X--------X-----    -_-  It's a Tie -_-   ---X-------X--------X----")
                break

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

        restart = input("Do You Want To Start Again? (Y/N) :")
        if restart == "Y" or restart == "y":
            for key in board_keys:
                theboard[key] = ' '

            game()
        else:
            print('\n\n')
            print('    ================================================================================================')
            print('    ||        ...............Hope u had the time of ur life!!!!!!!! SEE U SOON !!!!!!!..          ||')
            print('    ================================================================================================')



    game()

elif g == x == 1:
    def ask():
        sym = str(input("what do u choose (X OR O): "))
        if sym.upper() == 'X':
            print("it is your chance first:\n")

            def grdom():

                turn = 'X'
                count = 0

                for i in range(10):
                    printboard(theboard)
                    print("It's", turn, "'s turn, move to where?")  # in place of turn say 'it is [player name] turn'
                    move = str(input())
                    print(' ')
                    if move in board_keys:
                        board_keys.remove(move)

                    if theboard[move] == ' ':
                        theboard[move] = turn
                        count += 1
                    else:
                        print("The place is already filled, Please move elsewhere..")
                        continue
                    if count >= 5:
                        if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                            printboard(theboard)
                            print("Game Over.")
                            print("   ------X-------X----------X----   ", turn,
                                  "- you Won the match! :D  --------X--------X-------X--------- ")
                            break
                        elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                            printboard(theboard)
                            print("Game over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "-you Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "- you Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "- you Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "- you Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "- you Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "-you Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "- you Won the match! :D    --------X--------X-------X--------- ")
                            print(count)
                            break

                    print(count)
                    if count == 9:
                        print("Game Over. ")
                        print("-----X-------X--------X-----    -_-  It's a Tie -_-   ---X-------X--------X----")
                        break

                    if turn == 'X':
                        turn = 'O'
                        while turn == 'O':
                            m = random.randint(0, len(board_keys) - 1)
                            w = str(board_keys[m])
                            if w in board_keys:
                                board_keys.remove(w)
                            print(board_keys)

                            if theboard[w] == ' ':
                                theboard[w] = turn
                                count += 1

                            if count >= 5:
                                if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                                    printboard(theboard)
                                    print("Game Over.")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                                    printboard(theboard)
                                    print("Game over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                                    printboard(theboard)
                                    print("Game Over.")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break

                            if count == 9:
                                print("Game Over. ")
                                print("-----X-------X--------X-----    -_-  It's a Tie -_-   ---X-------X--------X----")

                            break
                        turn = 'X'
                    else:
                        turn = 'X'

                board_keys.clear()
                theboard['1'] = ' '
                theboard['2'] = ' '
                theboard['3'] = ' '
                theboard['4'] = ' '
                theboard['5'] = ' '
                theboard['6'] = ' '
                theboard['7'] = ' '
                theboard['8'] = ' '
                theboard['9'] = ' '

                def rest():
                    restart = input("Do You Want To Start Again? (Y/N) :")
                    if restart == "Y" or restart == "y":
                        theboard = {'1': ' ', '2': ' ', '3': ' ',
                                    '4': ' ', '5': ' ', '6': ' ',  # board format
                                    '7': ' ', '8': ' ', '9': ' '}
                        for key in theboard:
                            board_keys.append(key)

                        for key in board_keys:
                            theboard[key] = ' '
                            grdom()
                    else:
                        print('\n\n')
                        print('    ================================================================================================')
                        print('    ||        ...............Hope u had the time of ur life!!!!!!!! SEE U SOON !!!!!!!..          ||')
                        print('    ================================================================================================')



                rest()

            grdom()


        else:
            print("you get 'O' ....... GO ON!!! ITS REALLY A FUN GAME !!!! :D")
            print('')

            def gamerdom():

                turn = 'O'
                count = 0

                for i in range(10):
                    printboard(theboard)
                    print("It's", turn, "'s turn, move to where?")  # in place of turn say 'it is [player name] turn'
                    move = str(input())
                    print(' ')
                    if move in board_keys:
                        board_keys.remove(move)

                    if theboard[move] == ' ':
                        theboard[move] = turn
                        count += 1
                    else:
                        print("The place is already filled, Please move elsewhere..")
                        continue
                    if count >= 5:
                        if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                            printboard(theboard)
                            print("Game Over.")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                            printboard(theboard)
                            print("Game over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D   --------X--------X-------X--------- ")
                            break
                        elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                            printboard(theboard)
                            print("Game Over. ")
                            print("   ------X-------X----------X----   ", turn,
                                  "Won the match! :D    --------X--------X-------X--------- ")
                            break
                    if count == 9:
                        print("Game Over. ")
                        print("-----X-------X--------X-----    -_-  It's a Tie -_-   ---X-------X--------X----")
                        break

                    if turn == 'O':
                        turn = 'X'
                        while turn == 'X':
                            m = random.randint(0, len(board_keys) - 1)
                            w = str(board_keys[m])
                            left=[]
                            if w in board_keys:
                                board_keys.remove(w)
                            print(board_keys)

                            if theboard[w] == ' ':
                                theboard[w] = turn
                                count += 1

                            if count >= 5:
                                if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                                    printboard(theboard)
                                    print("Game Over.")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                                    printboard(theboard)
                                    print("Game over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                                elif theboard['3'] == theboard['5'] == theboard['7'] != ' ':
                                    printboard(theboard)
                                    print("Game Over. ")
                                    print(
                                        "   ------X-------X----------X----   COMPUTER !!!!! Won the match! :(  --------X--------X-------X--------- ")
                                    break
                            if count == 9:
                                print("Game Over. ")
                                print("-----X-------X--------X-----    -_-  It's a Tie -_-   ---X-------X--------X----")

                            break
                        turn = 'O'

                    else:
                        turn = 'O'
                board_keys.clear()
                theboard['1'] = ' '
                theboard['2'] = ' '
                theboard['3'] = ' '
                theboard['4'] = ' '
                theboard['5'] = ' '
                theboard['6'] = ' '
                theboard['7'] = ' '
                theboard['8'] = ' '
                theboard['9'] = ' '

                def re():
                    restart = input("Do You Want To Start Again? (Y/N) :")
                    if restart == "Y" or restart == "y":
                        theboard = {'1': ' ', '2': ' ', '3': ' ',
                                    '4': ' ', '5': ' ', '6': ' ',  # board format
                                    '7': ' ', '8': ' ', '9': ' '}
                        for key in theboard:
                            board_keys.append(key)

                        for key in board_keys:
                            theboard[key] = ' '
                            gamerdom()
                    else:
                        print('\n\n')
                        print('    ================================================================================================')
                        print('    ||        ...............Hope u had the time of ur life!!!!!!!! SEE U SOON !!!!!!!..          ||')
                        print('    ================================================================================================')

                re()
            gamerdom()


    ask()
