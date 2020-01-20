from .draw_a_game_board import editboard


def playgame(matrix, num, p1name, p2name):
    name = "abc"
    if num % 2 + 1 == 1:
        name = p1name
        print(p1name + ", what is your move (in terms of row, column)?")
    else:
        name = p2name
        print(p2name + ", what is your move (in terms of row, column)?")
    move = input()
    xy = move.split(",")
    x = int(xy[0]) - 1
    y = int(xy[1]) - 1
    if x < 3 and y < 3:
        if matrix[x][y] == 0:
            if num % 2 == 0:
                matrix[x][y] = "X"
            else:
                matrix[x][y] = "O"
            editboard(matrix)
        else:
            print("Invalid move")
            editboard(matrix)
            playgame(matrix, num)



