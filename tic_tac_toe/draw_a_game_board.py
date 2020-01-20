def dash():
    num = 0
    while num < 3:
        if num == 0:
            print(" --- ", end='')
        elif num == 2:
            print("--- ")
        else:
            print("--- ", end='')
        num += 1


def line():
    num = 0
    while num < 4:
        if num == 3:
            print("|")
        else:
            print("|   ", end='')
        num += 1


def editboard(matrix):
    dash()
    fill(matrix, 0)
    dash()
    fill(matrix, 1)
    dash()
    fill(matrix, 2)
    dash()


def fill(matrix, y):
    num = 0
    x = 0
    while num < 4:
        if num == 3:
            print("|")
        else:
            print("| ", end='')
            if matrix[x][y] != 0:
                print(matrix[x][y] + " ", end='')

            else:
                print("  ", end='')
            x += 1
        num += 1

