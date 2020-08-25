board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')
            if j == 8:
                print(str(bo[i][j]) + " ")
                continue
            print(str(bo[i][j]) + " ", end='')


def find_empty(bo):
    empty = []
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                empty.append((i, j))
    return empty


def validate(bo, pos, num):

    # Check the row

    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and j != pos[1]:
            return False  # fails check / there is a duplicate

    # Check the column

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    empty = find_empty(bo)
    counter = 0
    
    while True:
        try:
          temp = empty[counter]
        except:
          break
        counter += 1


solve(board)


