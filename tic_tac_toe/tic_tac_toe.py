from .draw_a_game_board import dash, line
from .check_tic_tac_toe import check, catsgame
from .tic_tac_toe_draw import playgame


def play(p1win, p2win, p1name, p2name):
    listofrows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    count = 0
    num = 0
    print("Which player is going first, " + p1name + " or " + p2name + "?")
    player = input()
    if player == p1name:
        num = 2
    else:
        num = 1
    while check(listofrows) == 0 and catsgame is not True:
        playgame(listofrows, num, p1name, p2name)
        num += 1
        count += 1
    winner = check(listofrows)
    if winner == 0:
        print("No Winner! Cat's Game")
    elif winner == "O":
        winplayer = p2name
        print("Congratulations " + p2name + "! You won!")
    else:
        winplayer = p1name
        print("Congratulations " + p1name + "! You won!")
    print("Would you like to play again? (y or n)")
    playagain = input()
    if playagain == "y":
        if winplayer == 1:
            p1win += 1
        elif winplayer == 2:
            p2win += 1
        print("The current score is " + p1name + ": " + str(p1win))
        print("                     " + p2name + ": " + str(p2win))
        play(p1win, p2win, p1name, p2name)
    else:
        print("Thanks for playing!")

