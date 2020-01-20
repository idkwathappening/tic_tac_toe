def check(matrix):
    for x in range(0, 3):
        row = set([matrix[x][0], matrix[x][1], matrix[x][2]])
        if len(row) == 1 and matrix[x][0] != 0:
            return matrix[x][0]
    for x in range(0, 3):
        column = set([matrix[0][x], matrix[1][x], matrix[2][x]])
        if len(column) == 1 and matrix[0][x] != 0:
            return matrix[0][x]
    diag1 = set([matrix[0][0], matrix[1][1], matrix[2][2]])
    diag2 = set([matrix[0][2], matrix[1][1], matrix[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and matrix[1][1] != 0:
        return matrix[1][1]
    return 0


def catsgame(matrix):
    for x in range(0, 3):
        for y in range(0, 3):
            if matrix[x][y] == 0:
                return False
            else:
                return True

